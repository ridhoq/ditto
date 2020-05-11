from ditto_markov.cosmos import cosmos


# @pytest.fixture(scope="module", autouse=True)
# def my_fixture():
#     print ('INITIALIZATION')
#     cosmos = DittoCosmos(COSMOS_ACCOUNT_URI, COSMOS_ACCOUNT_KEY, COSMOS_DATABASE_ID)
#     print ('TEAR DOWN')
    

def test_cosmos_client():
    assert cosmos is not None

