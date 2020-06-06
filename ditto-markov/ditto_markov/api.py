from fastapi import FastAPI
from cachetools import LFUCache

from .cache import CacheRepository, BlobCache
from .markov import get_model

api = FastAPI()

cache_repo = CacheRepository()

lfu_cache = LFUCache(maxsize=5)
cache_repo.register_cache("lfu", lfu_cache)

blob_cache = BlobCache()
cache_repo.register_cache("blob", blob_cache)


@api.get("/transform/{user}")
def get_transform(user):
    model = get_model(user, cache_repo)
    return {user: model.make_sentence()}
