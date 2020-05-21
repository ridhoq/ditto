from abc import ABC, abstractmethod
from collections import OrderedDict
import typing
from typing import Union

import cachetools


class Cache(ABC):
    @abstractmethod
    def __getitem__(self, key):
        raise NotImplementedError

    @abstractmethod
    def __setitem__(self, key, value):
        raise NotImplementedError

    @abstractmethod
    def __contains__(self, key):
        raise NotImplementedError


RegisterableCache = Union[Cache, cachetools.Cache]


class CacheRepository(Cache):
    caches: typing.OrderedDict[str, RegisterableCache]

    def __init__(self):
        self.caches = OrderedDict()

    def register_cache(self, name: str, cache: RegisterableCache):
        self.caches[name] = cache

    def get_caches(self):
        return list(self.caches.values())

    def __getitem__(self, key):
        for idx, item in enumerate(self.caches.items()):
            name, cache = item
            if key in cache:
                print(f"==================== {name} cache hit for {key} ====================")
                value = cache[key]

                # cache this value in prior caches for faster access
                for prior_cache in self.get_caches()[0:idx]:
                    prior_cache[key] = value
                return value
            else:
                pass
        raise KeyError

    def __setitem__(self, key, value):
        for cache in self.get_caches():
            cache[key] = value

    def __contains__(self, key):
        for cache in self.get_caches():
            if key in cache:
                return True

        return False
