from AllMethods.all_methods import get_categories, validate_jsonschema


def test_get_categories():
    response = get_categories()
    assert response.status_code == 200


def test_jsonschema_categories():
    schema = open("schemes/get_categories.json").read()
    response = get_categories()
    validate_jsonschema(schema, response)
