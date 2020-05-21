import pytest

from ditto_markov.cache.cache import CacheRepository
from ditto_markov.cache.simple import SimpleCache

cache_1 = SimpleCache()
cache_2 = SimpleCache()
cache_3 = SimpleCache()
cache_1["ayy"] = "lmao"
cache_2["yee"] = "haw"
cache_3["ping"] = "pong"
repo = CacheRepository()
repo.register_backend(cache_1)
repo.register_backend(cache_2)
repo.register_backend(cache_3)


def test_can_get_from_cache_repo():
    assert repo["ayy"] == "lmao"
    assert repo["yee"] == "haw"
    assert repo["ping"] == "pong"
    with pytest.raises(KeyError):
        return repo["nah"]


def test_contains_from_cache_repo():
    assert "ayy" in repo
    assert "yee" in repo
    assert "ping" in repo
    assert "nah" not in repo


def test_can_set_from_cache_repo():
    repo["woah"] = "dude"
    assert "woah" in repo
    assert repo["woah"] == "dude"
