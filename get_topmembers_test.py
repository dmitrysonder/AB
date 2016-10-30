from AllMethods.all_methods import get_topmembers


def test_get_topmembers():
    response = get_topmembers()
    assert response.status_code == 200


'''
def test_jsonschema_topmembers():
    schema = open("schemes/get_topmembers.json").read()
    response = get_topmembers()
    validate_jsonschema(schema, response)
'''
