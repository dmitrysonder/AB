from AllMethods.all_methods import get_charity_by_uuid, validate_jsonschema


def test_get_charity_by_uuid():
    response = get_charity_by_uuid()
    assert response.status_code == 200


def test_jsonschema_charity_by_uuid():
    schema = open("schemes/get_charity_by_uuid.json").read()
    response = get_charity_by_uuid()
    validate_jsonschema(schema, response)
