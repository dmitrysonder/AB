from AllMethods.all_methods import get_charities, validate_jsonschema


def test_get_charities():
    response = get_charities()
    assert response.status_code == 200


def test_jsonschema_charities():
    schema = open("schemes/get_charities.json").read()
    response = get_charities()
    validate_jsonschema(schema, response)
