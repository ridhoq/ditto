from azure.core.exceptions import ResourceNotFoundError, ResourceExistsError
from azure.storage.blob import BlobServiceClient

from .cache import Cache
from ..config import AZURE_STORAGE_CONNECTION_STRING


class BlobCache(Cache):
    container = "markov"
    _blob_service_client: BlobServiceClient

    def __init__(self):
        self._blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
        try:
            self._blob_service_client.create_container(self.container)
        except ResourceExistsError:
            pass

    def __getitem__(self, key):
        try:
            blob_client = self._blob_service_client.get_blob_client(container=self.container, blob=key)
            return blob_client.download_blob().readall()
        except ResourceNotFoundError:
            raise KeyError

    def __setitem__(self, key, value):
        blob_client = self._blob_service_client.get_blob_client(container=self.container, blob=key)
        blob_client.upload_blob(value, overwrite=True)

    def __contains__(self, key):
        container_client = self._blob_service_client.get_container_client(container=self.container)
        try:
            return key == container_client.list_blobs(name_starts_with=key).next().name
        except StopIteration:
            return False
