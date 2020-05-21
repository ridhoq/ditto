from abc import ABC, abstractmethod
from typing import List, Union

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


Backend = Union[Cache, cachetools.Cache]


class CacheRepository(Cache):
    caches: List[Backend]

    def __init__(self):
        self.caches = []

    def register_backend(self, backend: Backend):
        self.caches.append(backend)

    def __getitem__(self, key):
        for idx, cache in enumerate(self.caches):
            if key in cache:
                value = cache[key]
                # cache this value in prior caches for faster access
                for prior_cache in self.caches[0:idx]:
                    prior_cache[key] = value
                return value
            else:
                pass
        raise KeyError

    def __setitem__(self, key, value):
        for cache in self.caches:
            cache[key] = value

    def __contains__(self, key):
        for cache in self.caches:
            if key in cache:
                return True

        return False
