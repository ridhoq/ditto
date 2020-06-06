# ditto-markov
Rewrite of the markov chain functionality into a python service using a Cosmos data source

## Getting Started
Currently, there's a CLI wrapper to generate the user's chat messages and an API
1. copy `.env.example` to `.env` and drop in the correct values
1. `docker-compose run --rm cli <slack-user>` will return 20 messages that sound like the user. Optionally, pass a space delimited list of users
1. `docker-compose up api` will start the API
