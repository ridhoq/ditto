import pytest

from ditto_markov.cache import BlobCache


def test_init():
    cache = BlobCache()
    assert cache is not None


def test_get():
    cache = BlobCache()
    blob_client = cache._blob_service_client.get_blob_client(container=BlobCache.container, blob="ayy")
    blob_client.upload_blob("lmao", overwrite=True)
    assert cache["ayy"].decode() == "lmao"
    with pytest.raises(KeyError):
        return cache["nah"]


def test_set():
    cache = BlobCache()
    cache["ayy"] = "lmao"
    container_client = cache._blob_service_client.get_container_client(container=BlobCache.container)
    assert "ayy" == container_client.list_blobs(name_starts_with="ayy").next().name


def test_contains():
    cache = BlobCache()
    cache["ayy"] = "lmao"
    assert "ayy" in cache
    assert "nah" not in cache
