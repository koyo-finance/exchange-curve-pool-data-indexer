import json

ABI = json.loads("""[
 {
  "name": "TokenExchange",
  "inputs": [
   {
    "type": "address",
    "name": "buyer",
    "indexed": true
   },
   {
    "type": "int128",
    "name": "sold_id",
    "indexed": false
   },
   {
    "type": "uint256",
    "name": "tokens_sold",
    "indexed": false
   },
   {
    "type": "int128",
    "name": "bought_id",
    "indexed": false
   },
   {
    "type": "uint256",
    "name": "tokens_bought",
    "indexed": false
   }
  ],
  "anonymous": false,
  "type": "event"
 },
 {
  "name": "TokenExchangeUnderlying",
  "inputs": [
   {
    "type": "address",
    "name": "buyer",
    "indexed": true
   },
   {
    "type": "int128",
    "name": "sold_id",
    "indexed": false
   },
   {
    "type": "uint256",
    "name": "tokens_sold",
    "indexed": false
   },
   {
    "type": "int128",
    "name": "bought_id",
    "indexed": false
   },
   {
    "type": "uint256",
    "name": "tokens_bought",
    "indexed": false
   }
  ],
  "anonymous": false,
  "type": "event"
 },
 {
  "name": "AddLiquidity",
  "inputs": [
   {
    "type": "address",
    "name": "provider",
    "indexed": true
   },
   {
    "type": "uint256[2]",
    "name": "token_amounts",
    "indexed": false
   },
   {
    "type": "uint256[2]",
    "name": "fees",
    "indexed": false
   },
   {
    "type": "uint256",
    "name": "invariant",
    "indexed": false
   },
   {
    "type": "uint256",
    "name": "token_supply",
    "indexed": false
   }
  ],
  "anonymous": false,
  "type": "event"
 },
 {
  "name": "RemoveLiquidity",
  "inputs": [
   {
    "type": "address",
    "name": "provider",
    "indexed": true
   },
   {
    "type": "uint256[2]",
    "name": "token_amounts",
    "indexed": false
   },
   {
    "type": "uint256[2]",
    "name": "fees",
    "indexed": false
   },
   {
    "type": "uint256",
    "name": "token_supply",
    "indexed": false
   }
  ],
  "anonymous": false,
  "type": "event"
 },
 {
  "name": "RemoveLiquidityImbalance",
  "inputs": [
   {
    "type": "address",
    "name": "provider",
    "indexed": true
   },
   {
    "type": "uint256[2]",
    "name": "token_amounts",
    "indexed": false
   },
   {
    "type": "uint256[2]",
    "name": "fees",
    "indexed": false
   },
   {
    "type": "uint256",
    "name": "invariant",
    "indexed": false
   },
   {
    "type": "uint256",
    "name": "token_supply",
    "indexed": false
   }
  ],
  "anonymous": false,
  "type": "event"
 },
 {
  "name": "CommitNewAdmin",
  "inputs": [
   {
    "type": "uint256",
    "name": "deadline",
    "indexed": true,
    "unit": "sec"
   },
   {
    "type": "address",
    "name": "admin",
    "indexed": true
   }
  ],
  "anonymous": false,
  "type": "event"
 },
 {
  "name": "NewAdmin",
  "inputs": [
   {
    "type": "address",
    "name": "admin",
    "indexed": true
   }
  ],
  "anonymous": false,
  "type": "event"
 },
 {
  "name": "CommitNewParameters",
  "inputs": [
   {
    "type": "uint256",
    "name": "deadline",
    "indexed": true,
    "unit": "sec"
   },
   {
    "type": "uint256",
    "name": "A",
    "indexed": false
   },
   {
    "type": "uint256",
    "name": "fee",
    "indexed": false
   },
   {
    "type": "uint256",
    "name": "admin_fee",
    "indexed": false
   }
  ],
  "anonymous": false,
  "type": "event"
 },
 {
  "name": "NewParameters",
  "inputs": [
   {
    "type": "uint256",
    "name": "A",
    "indexed": false
   },
   {
    "type": "uint256",
    "name": "fee",
    "indexed": false
   },
   {
    "type": "uint256",
    "name": "admin_fee",
    "indexed": false
   }
  ],
  "anonymous": false,
  "type": "event"
 },
 {
  "outputs": [],
  "inputs": [
   {
    "type": "address[2]",
    "name": "_coins"
   },
   {
    "type": "address[2]",
    "name": "_underlying_coins"
   },
   {
    "type": "address",
    "name": "_pool_token"
   },
   {
    "type": "uint256",
    "name": "_A"
   },
   {
    "type": "uint256",
    "name": "_fee"
   }
  ],
  "constant": false,
  "payable": false,
  "type": "constructor"
 },
 {
  "name": "get_virtual_price",
  "outputs": [
   {
    "type": "uint256",
    "name": "out"
   }
  ],
  "inputs": [],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 1084167
 },
 {
  "name": "calc_token_amount",
  "outputs": [
   {
    "type": "uint256",
    "name": "out"
   }
  ],
  "inputs": [
   {
    "type": "uint256[2]",
    "name": "amounts"
   },
   {
    "type": "bool",
    "name": "deposit"
   }
  ],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 4239939
 },
 {
  "name": "add_liquidity",
  "outputs": [],
  "inputs": [
   {
    "type": "uint256[2]",
    "name": "amounts"
   },
   {
    "type": "uint256",
    "name": "min_mint_amount"
   }
  ],
  "constant": false,
  "payable": false,
  "type": "function",
  "gas": 6479997
 },
 {
  "name": "get_dy",
  "outputs": [
   {
    "type": "uint256",
    "name": "out"
   }
  ],
  "inputs": [
   {
    "type": "int128",
    "name": "i"
   },
   {
    "type": "int128",
    "name": "j"
   },
   {
    "type": "uint256",
    "name": "dx"
   }
  ],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2543681
 },
 {
  "name": "get_dx",
  "outputs": [
   {
    "type": "uint256",
    "name": "out"
   }
  ],
  "inputs": [
   {
    "type": "int128",
    "name": "i"
   },
   {
    "type": "int128",
    "name": "j"
   },
   {
    "type": "uint256",
    "name": "dy"
   }
  ],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2543687
 },
 {
  "name": "get_dy_underlying",
  "outputs": [
   {
    "type": "uint256",
    "name": "out"
   }
  ],
  "inputs": [
   {
    "type": "int128",
    "name": "i"
   },
   {
    "type": "int128",
    "name": "j"
   },
   {
    "type": "uint256",
    "name": "dx"
   }
  ],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2543506
 },
 {
  "name": "get_dx_underlying",
  "outputs": [
   {
    "type": "uint256",
    "name": "out"
   }
  ],
  "inputs": [
   {
    "type": "int128",
    "name": "i"
   },
   {
    "type": "int128",
    "name": "j"
   },
   {
    "type": "uint256",
    "name": "dy"
   }
  ],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2543512
 },
 {
  "name": "exchange",
  "outputs": [],
  "inputs": [
   {
    "type": "int128",
    "name": "i"
   },
   {
    "type": "int128",
    "name": "j"
   },
   {
    "type": "uint256",
    "name": "dx"
   },
   {
    "type": "uint256",
    "name": "min_dy"
   }
  ],
  "constant": false,
  "payable": false,
  "type": "function",
  "gas": 5184573
 },
 {
  "name": "exchange_underlying",
  "outputs": [],
  "inputs": [
   {
    "type": "int128",
    "name": "i"
   },
   {
    "type": "int128",
    "name": "j"
   },
   {
    "type": "uint256",
    "name": "dx"
   },
   {
    "type": "uint256",
    "name": "min_dy"
   }
  ],
  "constant": false,
  "payable": false,
  "type": "function",
  "gas": 5200817
 },
 {
  "name": "remove_liquidity",
  "outputs": [],
  "inputs": [
   {
    "type": "uint256",
    "name": "_amount"
   },
   {
    "type": "uint256[2]",
    "name": "min_amounts"
   }
  ],
  "constant": false,
  "payable": false,
  "type": "function",
  "gas": 153898
 },
 {
  "name": "remove_liquidity_imbalance",
  "outputs": [],
  "inputs": [
   {
    "type": "uint256[2]",
    "name": "amounts"
   },
   {
    "type": "uint256",
    "name": "max_burn_amount"
   }
  ],
  "constant": false,
  "payable": false,
  "type": "function",
  "gas": 6479708
 },
 {
  "name": "commit_new_parameters",
  "outputs": [],
  "inputs": [
   {
    "type": "uint256",
    "name": "amplification"
   },
   {
    "type": "uint256",
    "name": "new_fee"
   },
   {
    "type": "uint256",
    "name": "new_admin_fee"
   }
  ],
  "constant": false,
  "payable": false,
  "type": "function",
  "gas": 146105
 },
 {
  "name": "apply_new_parameters",
  "outputs": [],
  "inputs": [],
  "constant": false,
  "payable": false,
  "type": "function",
  "gas": 133512
 },
 {
  "name": "revert_new_parameters",
  "outputs": [],
  "inputs": [],
  "constant": false,
  "payable": false,
  "type": "function",
  "gas": 21835
 },
 {
  "name": "commit_transfer_ownership",
  "outputs": [],
  "inputs": [
   {
    "type": "address",
    "name": "_owner"
   }
  ],
  "constant": false,
  "payable": false,
  "type": "function",
  "gas": 74512
 },
 {
  "name": "apply_transfer_ownership",
  "outputs": [],
  "inputs": [],
  "constant": false,
  "payable": false,
  "type": "function",
  "gas": 60568
 },
 {
  "name": "revert_transfer_ownership",
  "outputs": [],
  "inputs": [],
  "constant": false,
  "payable": false,
  "type": "function",
  "gas": 21925
 },
 {
  "name": "withdraw_admin_fees",
  "outputs": [],
  "inputs": [],
  "constant": false,
  "payable": false,
  "type": "function",
  "gas": 12831
 },
 {
  "name": "kill_me",
  "outputs": [],
  "inputs": [],
  "constant": false,
  "payable": false,
  "type": "function",
  "gas": 37878
 },
 {
  "name": "unkill_me",
  "outputs": [],
  "inputs": [],
  "constant": false,
  "payable": false,
  "type": "function",
  "gas": 22015
 },
 {
  "name": "coins",
  "outputs": [
   {
    "type": "address",
    "name": "out"
   }
  ],
  "inputs": [
   {
    "type": "int128",
    "name": "arg0"
   }
  ],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2190
 },
 {
  "name": "underlying_coins",
  "outputs": [
   {
    "type": "address",
    "name": "out"
   }
  ],
  "inputs": [
   {
    "type": "int128",
    "name": "arg0"
   }
  ],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2220
 },
 {
  "name": "balances",
  "outputs": [
   {
    "type": "uint256",
    "name": "out"
   }
  ],
  "inputs": [
   {
    "type": "int128",
    "name": "arg0"
   }
  ],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2250
 },
 {
  "name": "A",
  "outputs": [
   {
    "type": "uint256",
    "name": "out"
   }
  ],
  "inputs": [],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2081
 },
 {
  "name": "fee",
  "outputs": [
   {
    "type": "uint256",
    "name": "out"
   }
  ],
  "inputs": [],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2111
 },
 {
  "name": "admin_fee",
  "outputs": [
   {
    "type": "uint256",
    "name": "out"
   }
  ],
  "inputs": [],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2141
 },
 {
  "name": "owner",
  "outputs": [
   {
    "type": "address",
    "name": "out"
   }
  ],
  "inputs": [],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2171
 },
 {
  "name": "admin_actions_deadline",
  "outputs": [
   {
    "type": "uint256",
    "unit": "sec",
    "name": "out"
   }
  ],
  "inputs": [],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2201
 },
 {
  "name": "transfer_ownership_deadline",
  "outputs": [
   {
    "type": "uint256",
    "unit": "sec",
    "name": "out"
   }
  ],
  "inputs": [],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2231
 },
 {
  "name": "future_A",
  "outputs": [
   {
    "type": "uint256",
    "name": "out"
   }
  ],
  "inputs": [],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2261
 },
 {
  "name": "future_fee",
  "outputs": [
   {
    "type": "uint256",
    "name": "out"
   }
  ],
  "inputs": [],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2291
 },
 {
  "name": "future_admin_fee",
  "outputs": [
   {
    "type": "uint256",
    "name": "out"
   }
  ],
  "inputs": [],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2321
 },
 {
  "name": "future_owner",
  "outputs": [
   {
    "type": "address",
    "name": "out"
   }
  ],
  "inputs": [],
  "constant": true,
  "payable": false,
  "type": "function",
  "gas": 2351
 }
]""")

TOKEN_ABI = json.loads("""[
    {
        "constant": true,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_spender",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_from",
                "type": "address"
            },
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            },
            {
                "name": "_spender",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "payable": true,
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "from",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "to",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    }
]""")

NEW_ABI = json.loads("""
[
 {
  "anonymous": false,
  "inputs": [
   {
    "indexed": true,
    "name": "buyer",
    "type": "address"
   },
   {
    "indexed": false,
    "name": "sold_id",
    "type": "int128"
   },
   {
    "indexed": false,
    "name": "tokens_sold",
    "type": "uint256"
   },
   {
    "indexed": false,
    "name": "bought_id",
    "type": "int128"
   },
   {
    "indexed": false,
    "name": "tokens_bought",
    "type": "uint256"
   }
  ],
  "name": "TokenExchange",
  "type": "event"
 },
 {
  "anonymous": false,
  "inputs": [
   {
    "indexed": true,
    "name": "buyer",
    "type": "address"
   },
   {
    "indexed": false,
    "name": "sold_id",
    "type": "int128"
   },
   {
    "indexed": false,
    "name": "tokens_sold",
    "type": "uint256"
   },
   {
    "indexed": false,
    "name": "bought_id",
    "type": "int128"
   },
   {
    "indexed": false,
    "name": "tokens_bought",
    "type": "uint256"
   }
  ],
  "name": "TokenExchangeUnderlying",
  "type": "event"
 },
 {
  "anonymous": false,
  "inputs": [
   {
    "indexed": true,
    "name": "provider",
    "type": "address"
   },
   {
    "indexed": false,
    "name": "token_amounts",
    "type": "uint256[2]"
   },
   {
    "indexed": false,
    "name": "fees",
    "type": "uint256[2]"
   },
   {
    "indexed": false,
    "name": "invariant",
    "type": "uint256"
   },
   {
    "indexed": false,
    "name": "token_supply",
    "type": "uint256"
   }
  ],
  "name": "AddLiquidity",
  "type": "event"
 },
 {
  "anonymous": false,
  "inputs": [
   {
    "indexed": true,
    "name": "provider",
    "type": "address"
   },
   {
    "indexed": false,
    "name": "token_amounts",
    "type": "uint256[2]"
   },
   {
    "indexed": false,
    "name": "fees",
    "type": "uint256[2]"
   },
   {
    "indexed": false,
    "name": "token_supply",
    "type": "uint256"
   }
  ],
  "name": "RemoveLiquidity",
  "type": "event"
 },
 {
  "anonymous": false,
  "inputs": [
   {
    "indexed": true,
    "name": "provider",
    "type": "address"
   },
   {
    "indexed": false,
    "name": "token_amount",
    "type": "uint256"
   },
   {
    "indexed": false,
    "name": "coin_amount",
    "type": "uint256"
   }
  ],
  "name": "RemoveLiquidityOne",
  "type": "event"
 },
 {
  "anonymous": false,
  "inputs": [
   {
    "indexed": true,
    "name": "provider",
    "type": "address"
   },
   {
    "indexed": false,
    "name": "token_amounts",
    "type": "uint256[2]"
   },
   {
    "indexed": false,
    "name": "fees",
    "type": "uint256[2]"
   },
   {
    "indexed": false,
    "name": "invariant",
    "type": "uint256"
   },
   {
    "indexed": false,
    "name": "token_supply",
    "type": "uint256"
   }
  ],
  "name": "RemoveLiquidityImbalance",
  "type": "event"
 },
 {
  "anonymous": false,
  "inputs": [
   {
    "indexed": true,
    "name": "deadline",
    "type": "uint256"
   },
   {
    "indexed": true,
    "name": "admin",
    "type": "address"
   }
  ],
  "name": "CommitNewAdmin",
  "type": "event"
 },
 {
  "anonymous": false,
  "inputs": [
   {
    "indexed": true,
    "name": "admin",
    "type": "address"
   }
  ],
  "name": "NewAdmin",
  "type": "event"
 },
 {
  "anonymous": false,
  "inputs": [
   {
    "indexed": true,
    "name": "deadline",
    "type": "uint256"
   },
   {
    "indexed": false,
    "name": "fee",
    "type": "uint256"
   },
   {
    "indexed": false,
    "name": "admin_fee",
    "type": "uint256"
   }
  ],
  "name": "CommitNewFee",
  "type": "event"
 },
 {
  "anonymous": false,
  "inputs": [
   {
    "indexed": false,
    "name": "fee",
    "type": "uint256"
   },
   {
    "indexed": false,
    "name": "admin_fee",
    "type": "uint256"
   }
  ],
  "name": "NewFee",
  "type": "event"
 },
 {
  "anonymous": false,
  "inputs": [
   {
    "indexed": false,
    "name": "old_A",
    "type": "uint256"
   },
   {
    "indexed": false,
    "name": "new_A",
    "type": "uint256"
   },
   {
    "indexed": false,
    "name": "initial_time",
    "type": "uint256"
   },
   {
    "indexed": false,
    "name": "future_time",
    "type": "uint256"
   }
  ],
  "name": "RampA",
  "type": "event"
 },
 {
  "anonymous": false,
  "inputs": [
   {
    "indexed": false,
    "name": "A",
    "type": "uint256"
   },
   {
    "indexed": false,
    "name": "t",
    "type": "uint256"
   }
  ],
  "name": "StopRampA",
  "type": "event"
 },
 {
  "inputs": [
   {
    "name": "_owner",
    "type": "address"
   },
   {
    "name": "_coins",
    "type": "address[2]"
   },
   {
    "name": "_pool_token",
    "type": "address"
   },
   {
    "name": "_A",
    "type": "uint256"
   },
   {
    "name": "_fee",
    "type": "uint256"
   },
   {
    "name": "_admin_fee",
    "type": "uint256"
   }
  ],
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "constructor",
  "name": "constructor"
 },
 {
  "gas": 5227,
  "inputs": [],
  "name": "A",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 955150,
  "inputs": [],
  "name": "get_virtual_price",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 3797461,
  "inputs": [
   {
    "name": "amounts",
    "type": "uint256[2]"
   },
   {
    "name": "deposit",
    "type": "bool"
   }
  ],
  "name": "calc_token_amount",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 5836477,
  "inputs": [
   {
    "name": "amounts",
    "type": "uint256[2]"
   },
   {
    "name": "min_mint_amount",
    "type": "uint256"
   }
  ],
  "name": "add_liquidity",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 2317363,
  "inputs": [
   {
    "name": "i",
    "type": "int128"
   },
   {
    "name": "j",
    "type": "int128"
   },
   {
    "name": "dx",
    "type": "uint256"
   }
  ],
  "name": "get_dy",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2317058,
  "inputs": [
   {
    "name": "i",
    "type": "int128"
   },
   {
    "name": "j",
    "type": "int128"
   },
   {
    "name": "dx",
    "type": "uint256"
   }
  ],
  "name": "get_dy_underlying",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2454671,
  "inputs": [
   {
    "name": "i",
    "type": "int128"
   },
   {
    "name": "j",
    "type": "int128"
   },
   {
    "name": "dx",
    "type": "uint256"
   },
   {
    "name": "min_dy",
    "type": "uint256"
   }
  ],
  "name": "exchange",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 143246,
  "inputs": [
   {
    "name": "_amount",
    "type": "uint256"
   },
   {
    "name": "min_amounts",
    "type": "uint256[2]"
   }
  ],
  "name": "remove_liquidity",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 5836308,
  "inputs": [
   {
    "name": "amounts",
    "type": "uint256[2]"
   },
   {
    "name": "max_burn_amount",
    "type": "uint256"
   }
  ],
  "name": "remove_liquidity_imbalance",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 1102,
  "inputs": [
   {
    "name": "_token_amount",
    "type": "uint256"
   },
   {
    "name": "i",
    "type": "int128"
   }
  ],
  "name": "calc_withdraw_one_coin",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 3660494,
  "inputs": [
   {
    "name": "_token_amount",
    "type": "uint256"
   },
   {
    "name": "i",
    "type": "int128"
   },
   {
    "name": "min_amount",
    "type": "uint256"
   }
  ],
  "name": "remove_liquidity_one_coin",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 151919,
  "inputs": [
   {
    "name": "_future_A",
    "type": "uint256"
   },
   {
    "name": "_future_time",
    "type": "uint256"
   }
  ],
  "name": "ramp_A",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 148637,
  "inputs": [],
  "name": "stop_ramp_A",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 110461,
  "inputs": [
   {
    "name": "new_fee",
    "type": "uint256"
   },
   {
    "name": "new_admin_fee",
    "type": "uint256"
   }
  ],
  "name": "commit_new_fee",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 97242,
  "inputs": [],
  "name": "apply_new_fee",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 21895,
  "inputs": [],
  "name": "revert_new_parameters",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 74572,
  "inputs": [
   {
    "name": "_owner",
    "type": "address"
   }
  ],
  "name": "commit_transfer_ownership",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 60710,
  "inputs": [],
  "name": "apply_transfer_ownership",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 21985,
  "inputs": [],
  "name": "revert_transfer_ownership",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 3481,
  "inputs": [
   {
    "name": "i",
    "type": "uint256"
   }
  ],
  "name": "admin_balances",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 9218,
  "inputs": [],
  "name": "withdraw_admin_fees",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 74965,
  "inputs": [],
  "name": "donate_admin_fees",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 37998,
  "inputs": [],
  "name": "kill_me",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 22135,
  "inputs": [],
  "name": "unkill_me",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
 },
 {
  "gas": 2220,
  "inputs": [
   {
    "name": "arg0",
    "type": "uint256"
   }
  ],
  "name": "coins",
  "outputs": [
   {
    "name": "",
    "type": "address"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2250,
  "inputs": [
   {
    "name": "arg0",
    "type": "uint256"
   }
  ],
  "name": "balances",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2171,
  "inputs": [],
  "name": "fee",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2201,
  "inputs": [],
  "name": "admin_fee",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2231,
  "inputs": [],
  "name": "owner",
  "outputs": [
   {
    "name": "",
    "type": "address"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2261,
  "inputs": [],
  "name": "initial_A",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2291,
  "inputs": [],
  "name": "future_A",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2321,
  "inputs": [],
  "name": "initial_A_time",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2351,
  "inputs": [],
  "name": "future_A_time",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2381,
  "inputs": [],
  "name": "admin_actions_deadline",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2411,
  "inputs": [],
  "name": "transfer_ownership_deadline",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2441,
  "inputs": [],
  "name": "future_fee",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2471,
  "inputs": [],
  "name": "future_admin_fee",
  "outputs": [
   {
    "name": "",
    "type": "uint256"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 },
 {
  "gas": 2501,
  "inputs": [],
  "name": "future_owner",
  "outputs": [
   {
    "name": "",
    "type": "address"
   }
  ],
  "stateMutability": "view",
  "type": "function"
 }
]
""")
