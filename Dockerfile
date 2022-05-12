FROM python@sha256:6b18b86cc686c9ddfc683f0a87b23105d4b2534bde813bbacfc26e7511e884cb

WORKDIR /usr/src/app

RUN pip install pipenv

# Copy and install Pipfile before everything else for better caching
COPY Pipfile* ./

# Sync (install) packages
RUN PIP_NO_CACHE_DIR=true pipenv install --system --deploy --dev --ignore-pipfile

COPY . .

COPY ./docker-entrypoint.sh /usr/local/bin/

CMD ["docker-entrypoint.sh"]
