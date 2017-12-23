# Ditto

## Installation

`cp .env.example .env`

Then change the .env contents to the proper values.

`docker-compose build`

then run:

`docker-compose up`

## Deploy to heroku

https://devcenter.heroku.com/articles/container-registry-and-runtime#pushing-an-image-s

`heroku container:push worker`

