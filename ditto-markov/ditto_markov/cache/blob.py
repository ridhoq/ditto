from azure.core.exceptions import ResourceNotFoundError
from azure.storage.blob import BlobServiceClient

from .cache import Cache
from ..config import AZURE_STORAGE_CONNECTION_STRING


class BlobCache(Cache):
    blob_service_client: BlobServiceClient

    def __init__(self):
        self.blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
        self.container = "markov"

    def __getitem__(self, key):
        try:
            blob_client = self.blob_service_client.get_blob_client(container=self.container, blob=key)
            print(f"cache hit for {key}")
            return blob_client.download_blob().readall()
        except ResourceNotFoundError:
            print(f"cache miss for {key}")
            raise KeyError

    def __setitem__(self, key, value):
        blob_client = self.blob_service_client.get_blob_client(container=self.container, blob=key)
        print(f"uploading blob for {key}")
        blob_client.upload_blob(value, overwrite=True)

    # TODO: azure docs failed me, we're going with this for now
    def __contains__(self, key):
        try:
            blob_client = self.blob_service_client.get_blob_client(container=self.container, blob=key)
            print(f"cache hit for {key}")
            return True if blob_client.download_blob().readall() else False
        except ResourceNotFoundError:
            return False
        pass
