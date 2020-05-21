from .cache import Cache
from typing import Dict


class SimpleCache(Cache):
    _cache: Dict

    def __init__(self):
        self._cache = {}

    def __getitem__(self, key):
        return self._cache[key]

    def __setitem__(self, key, value):
        self._cache[key] = value

    def __contains__(self, key):
        return key in self._cache

