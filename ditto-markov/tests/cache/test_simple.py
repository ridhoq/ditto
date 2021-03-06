import pytest

from ditto_markov.cache import SimpleCache


def test_get():
    cache = SimpleCache()
    cache._cache["ayy"] = "lmao"
    assert cache["ayy"] == "lmao"
    with pytest.raises(KeyError):
        return cache["nah"]


def test_set():
    cache = SimpleCache()
    cache["ayy"] = "lmao"
    assert cache._cache["ayy"] == "lmao"


def test_contains():
    cache = SimpleCache()
    cache["ayy"] = "lmao"
    assert "ayy" in cache
