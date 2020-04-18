FROM elixir:1.4

RUN useradd -ms /bin/bash ditto
USER ditto
WORKDIR /home/ditto

CMD ["mix", "run", "--no-halt"]

RUN mix local.hex --force && \
    mix local.rebar --force

COPY mix.exs /home/ditto/mix.exs
# COPY mix.lock /home/ditto/mix.lock

RUN mix deps.get

COPY lib /home/ditto/lib
COPY config /home/ditto/config
COPY test /home/ditto/test
