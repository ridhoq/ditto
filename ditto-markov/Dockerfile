FROM python:3.7.3-alpine as base

WORKDIR /app

RUN apk add --update --no-cache --virtual .build-deps \
    gcc \
    libffi-dev \
    musl-dev \
    postgresql-dev \
    python-dev \
 && echo ':^)'

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.5 \
    HOME=/root

# install poetry
RUN wget -qO- https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
 && echo 'export PATH=$PATH:$HOME/.poetry/bin' > /etc/profile.d/poetry.sh \
 && $HOME/.poetry/bin/poetry config virtualenvs.create false 

ENV PATH $HOME/.poetry/bin:$PATH

COPY pyproject.toml poetry.lock ./
RUN mkdir -p ditto_markov/ && touch ditto_markov/__init__.py
RUN poetry install --no-dev

FROM base as production

RUN apk del .build-deps

COPY . .

FROM base as development

RUN $HOME/.poetry/bin/poetry install
