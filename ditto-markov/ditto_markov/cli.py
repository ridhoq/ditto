import sys

from .cache import CacheRepository, BlobCache
from .markov import get_model

team_ayy_lmao_users = {
    'd': 'U0316HMAS',
    'tom': 'U034S6QF6',
    'austin': 'U03169VDW',
    'rid': 'U0314Q64M',
    'thomas': 'U031D6P73',
    'matty': 'U03LTN7RH',
    'beej': 'U03JA1HKP',
    'nickpray': 'U09BC6LR5',
    'partypat': 'U22RC4XB2'
}


def main():
    for user_name in sys.argv[1:]:
        user = team_ayy_lmao_users[user_name]

        cache_repo = CacheRepository()
        blob_backend = BlobCache()
        cache_repo.register_backend(blob_backend)

        model = get_model(user, cache_repo)
        for i in range(20):
            print(model.make_sentence())
