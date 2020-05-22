import json

import azure.cosmos.documents as documents
import pytest
from azure.cosmos import errors, http_constants

from ditto_markov.cosmos import cosmos, events_container_id


def test_cosmos_client_exists():
    assert cosmos is not None


def test_can_get_events_for_user():
    rid = "U0314Q64M"
    rid_events = cosmos.get_message_events_for_user(rid)
    assert rid_events is not None
    assert len_iterable(rid_events) == 4


@pytest.fixture(scope="module", autouse=True)
def cosmos_fixture(request):
    try:
        cosmos.cosmos.CreateDatabase({'id': cosmos.database_id})
    except errors.HTTPFailure:
        pass
    container_definition = {'id': events_container_id,
                            'partitionKey':
                                {
                                    'paths': ['/user'],
                                    'kind': documents.PartitionKind.Hash
                                }
                            }
    try:
        cosmos.cosmos.CreateContainer(cosmos_db_id(), container_definition)
    except errors.HTTPFailure as e:
        if e.status_code == http_constants.StatusCodes.CONFLICT:
            pass
        else:
            raise e

    with open("tests/messages.json") as f:
        for item in json.load(f):
            cosmos.cosmos.UpsertItem(cosmos.get_container_path(events_container_id), item)
    request.addfinalizer(cosmos_cleanup)


def cosmos_cleanup():
    cosmos.cosmos.DeleteDatabase(cosmos_db_id())


def len_iterable(iterable):
    return sum([1 for _ in iterable])


def cosmos_db_id():
    return f"dbs/{cosmos.database_id}"
