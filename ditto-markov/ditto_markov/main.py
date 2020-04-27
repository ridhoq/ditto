import os
import json

import azure.cosmos.cosmos_client as cosmos_client
import markovify

# from config import COSMOS_ACCOUNT_URI, COSMOS_ACCOUNT_KEY

COSMOS_ACCOUNT_URI = os.environ['COSMOS_ACCOUNT_URI']
COSMOS_ACCOUNT_KEY = os.environ['COSMOS_ACCOUNT_KEY']

client = cosmos_client.CosmosClient(COSMOS_ACCOUNT_URI, {'masterKey': COSMOS_ACCOUNT_KEY})

database_id = 'team-ayy-lmao'
container_id = 'slack-events'
cosmos_path = f'dbs/{database_id}/colls/{container_id}'

# @d
# user = 'U0316HMAS'
# @tom
# user = 'U034S6QF6'
# @austin
# user = 'U03169VDW'
# @rid
user = 'U0314Q64M'
# @thomas
# user = 'U031D6P73'
# @matty
# user = 'U03LTN7RH'
# @beej
# user = 'U03JA1HKP'
# @nickpray
# user = 'U09BC6LR5'

query = f'SELECT * FROM events e where e.user = "{user}" and e.type = "message" order by e.ts desc'

def main():
  messages = [ item["text"] for item in client.QueryItems(cosmos_path, query) ]
  newline_delimited_messages = "\n".join(messages)

  model = markovify.NewlineText(newline_delimited_messages)
  for i in range(20):
    print(model.make_sentence())
