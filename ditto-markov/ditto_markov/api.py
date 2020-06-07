import sys

from fastapi import FastAPI, HTTPException
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
    try:
        model = get_model(user, cache_repo)
        return {user: [model.make_sentence() for _ in range(20)]}
    except KeyError:
        raise HTTPException(status_code=404, detail="user not found")
