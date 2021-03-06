import os
from distutils.util import strtobool

COSMOS_ACCOUNT_URI = os.getenv('COSMOS_ACCOUNT_URI')
COSMOS_ACCOUNT_KEY = os.getenv('COSMOS_ACCOUNT_KEY')
COSMOS_DATABASE_ID = os.getenv('COSMOS_DATABASE_ID')
AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
COSMOS_DISABLE_TLS = bool(strtobool(os.getenv('COSMOS_DISABLE_TLS') or "False"))
