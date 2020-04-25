import os
import azure.cosmos.cosmos_client as cosmos_client
import json

from config import COSMOS_ACCOUNT_URI, COSMOS_ACCOUNT_KEY

# COSMOS_ACCOUNT_URI = os.environ['COSMOS_ACCOUNT_URI']
# COSMOS_ACCOUNT_KEY = os.environ['COSMOS_ACCOUNT_KEY']

client = cosmos_client.CosmosClient(COSMOS_ACCOUNT_URI, {'masterKey': COSMOS_ACCOUNT_KEY})
database_id = 'team-ayy-lmao'
container_id = 'slack-events'


for item in client.QueryItems("dbs/" + database_id + "/colls/" + container_id, 'SELECT TOP 100 * FROM events e where e.user = "U0316HMAS" and e.type = "message" order by e.ts desc'):
  print(json.dumps(item, indent=True))
