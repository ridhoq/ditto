import azure.cosmos.cosmos_client as cosmos_client

from .config import COSMOS_ACCOUNT_URI, COSMOS_ACCOUNT_KEY, COSMOS_DATABASE_ID

events_container_id = 'slack-events'


class DittoCosmos:
    def __init__(self, cosmos_account_uri, cosmos_account_key, cosmos_database_id):
        self.cosmos = cosmos_client.CosmosClient(cosmos_account_uri, {'masterKey': cosmos_account_key})
        self.database_id = cosmos_database_id

    def get_container_path(self, container_id):
        return f"dbs/{self.database_id}/colls/{container_id}"

    def get_message_events_for_user(self, user):
        query = """
      SELECT * 
      FROM events e
      WHERE e.user = @user
      AND e.type = "message"
      ORDER BY e.ts DESC
    """
        return self.cosmos.QueryItems(
            self.get_container_path(events_container_id),
            {
                'query': query,
                'parameters': [
                    {'name': '@user', 'value': user}
                ]
            },
            partition_key=user
        )


cosmos = DittoCosmos(COSMOS_ACCOUNT_URI, COSMOS_ACCOUNT_KEY, COSMOS_DATABASE_ID)
