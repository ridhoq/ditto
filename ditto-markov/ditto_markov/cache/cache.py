from abc import ABC, abstractmethod


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


class CacheRepository:
    caches: list[Cache]

    def __init__(self):
        self.caches = []

    def register_backend(self, cache: Cache):
        self.caches.append(cache)

    def __getitem__(self, key):
        for cache in self.caches:
            if key in cache:
                return cache[key]
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
