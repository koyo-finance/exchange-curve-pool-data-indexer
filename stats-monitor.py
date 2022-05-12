#!/usr/bin/env python3

import os
import lmdb
import json
from multiprocessing import get_context
import time
from time import sleep
from functools import partial
from loguru import logger
from web3.middleware import geth_poa_middleware

from koyostats.newpool import NewPool

MPOOL_SIZE = 100
DB_NAME = 'koyostats.lmdb'  # <- DB [block][pool#]{...}
CUSTOM_NODE = "http://mainnet.boba.node.koyo.finance/rpc"

os.environ["WEB3_HTTP_PROVIDER_URI"] = CUSTOM_NODE

pools = {
        '4pool': (NewPool, ("0x9F0a572be1Fcfe96E94C0a730C5F4bc2993fe3F6", "0xDAb3Fc342A242AdD09504bea790f9b026Aa1e709"), 579_236),
}
start_blocks = {}


from web3.auto.http import w3
w3.middleware_onion.inject(geth_poa_middleware, layer=0)


def init_pools():
    for i, p in pools.items():
        if isinstance(p, tuple):
            pools[i] = p[0](*p[1])
            start_blocks[i] = p[2]


def fetch_stats(block, i='4pool'):
    init_pools()
    return pools[i].fetch_stats(block)


def int2uid(value):
    return int.to_bytes(value, 4, 'big')


def pools_not_in_block(tx, b):
    out = []
    block = tx.get(int2uid(b))
    if block:
        block = json.loads(block)
    if block:
        for k in pools:
            if k not in block:
                out.append(k)
    else:
        out = list(pools)
    return out


mpool = get_context("fork").Pool(MPOOL_SIZE)
init_pools()


if __name__ == '__main__':
    init_pools()

    db = lmdb.open(DB_NAME, map_size=(2 ** 35))

    start_block = 579_200
    # start_block = w3.eth.getBlock('latest')['number'] - 1000
    logger.info('Monitor started')

    # Initial data
    with db.begin(write=True) as tx:
        if pools_not_in_block(tx, 0) or True:  # XXX
            tx.put(int2uid(0), json.dumps(
                        {k: {
                            'N': pool.N,
                            'underlying_N': pool.underlying_N if hasattr(pool, 'underlying_N') else pool.N,
                            'decimals': pool.decimals,
                            'underlying_decimals': pool.underlying_decimals if hasattr(pool, 'underlying_decimals') else pool.decimals,
                            'token': pool.token.address, 'pool': pool.pool.address,
                            'coins': [pool.coins[j].address for j in range(pool.N)],
                            'underlying_coins': [pool.underlying_coins[j].address for j in range(getattr(pool, 'underlying_N', pool.N))]}
                         for k, pool in pools.items()}).encode())

    while True:
        while True:
            try:
                current_block = w3.eth.getBlock('latest')['number'] + 1
                break
            except Exception:
                time.sleep(10)

        if current_block - start_block > MPOOL_SIZE:
            blocks = range(start_block, start_block + MPOOL_SIZE)
            with db.begin(write=True) as tx:
                pools_to_fetch = pools_not_in_block(tx, blocks[-1])
                if pools_to_fetch:
                    stats = {}
                    for p in pools_to_fetch:
                        if blocks[0] >= start_blocks[p]:
                            newstats = mpool.map(partial(fetch_stats, i=p), blocks)
                            for b, s in zip(blocks, newstats):
                                if b not in stats:
                                    stats[b] = {}
                                stats[b][p] = s
                    for b, v in stats.items():
                        block = tx.get(int2uid(b))
                        if block:
                            block = json.loads(block)
                            v.update(block)
                        tx.put(int2uid(b), json.dumps(v).encode())
                    pools_fetched = [p for p in pools_to_fetch
                                     if blocks[-1] in stats and p in stats[blocks[-1]]]
                    logger.info('... {} {}', start_block, str(pools_fetched))
                else:
                    logger.info('... already in DB: {}', start_block)
            start_block += MPOOL_SIZE
        else:
            if current_block > start_block:
                for block in range(start_block, current_block):
                    with db.begin(write=True) as tx:
                        if pools_not_in_block(tx, block):
                            stats = {}
                            for p, pool in pools.items():
                                if block >= start_blocks[p]:
                                    stats[p] = pool.fetch_stats(block)
                            logger.debug("{} {}", block, str([len(s['trades']) for s in stats.values()]))
                            tx.put(int2uid(block), json.dumps(stats).encode())
                start_block = current_block

            sleep(3)
