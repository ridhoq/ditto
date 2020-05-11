import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import urllib3

from .config import COSMOS_ACCOUNT_URI, COSMOS_ACCOUNT_KEY, COSMOS_DATABASE_ID, COSMOS_ENABLE_TLS

events_container_id = 'slack-events'


class DittoCosmos:
    def __init__(self, cosmos_account_uri, cosmos_account_key, cosmos_database_id, cosmos_enable_tls=True):
        connection_policy = documents.ConnectionPolicy()
        connection_policy.SSLConfiguration = documents.SSLConfiguration()
        if cosmos_enable_tls:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            connection_policy.SSLConfiguration.SSLCaCerts = False
        self.cosmos = cosmos_client.CosmosClient(cosmos_account_uri, {'masterKey': cosmos_account_key}, connection_policy)
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


cosmos = DittoCosmos(COSMOS_ACCOUNT_URI, COSMOS_ACCOUNT_KEY, COSMOS_DATABASE_ID, COSMOS_ENABLE_TLS)
