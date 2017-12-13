FROM elixir:1.4

WORKDIR /ditto

CMD ["mix", "run", "--no-halt"]

RUN mix local.hex --force && \
    mix local.rebar --force

COPY mix.exs /ditto/mix.exs
COPY mix.lock /ditto/mix.lock

RUN mix deps.get

COPY lib /ditto/lib
COPY config /ditto/config
COPY test /ditto/test
