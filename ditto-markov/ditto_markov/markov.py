from azure.core.exceptions import ResourceNotFoundError
from azure.storage.blob import BlobServiceClient
import markovify

from .cosmos import cosmos
from .config import AZURE_STORAGE_CONNECTION_STRING

blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
container = "markov"

def get_model(user):
  cached_model = get_cached_model(user)
  if cached_model:
    return cached_model
  
  messages = [item["text"] for item in cosmos.get_message_events_for_user(user)]
  newline_delimited_messages = "\n".join(messages)
  model = markovify.NewlineText(newline_delimited_messages)
  write_model_to_blob_storage(user, model.to_json())

  return model

def get_cached_model(user):
  try:
    blob_client = blob_service_client.get_blob_client(container=container, blob=user)
    model_json = blob_client.download_blob().readall()
    print(f"cache hit for {user}")
    return markovify.NewlineText.from_json(model_json)
  except ResourceNotFoundError:
    print(f"cache miss for {user}")
    return None

def write_model_to_blob_storage(user, model):
  blob_client = blob_service_client.get_blob_client(container=container, blob=user)
  print(f"uploading blob for {user}")
  blob_client.upload_blob(model, overwrite=True)
  
