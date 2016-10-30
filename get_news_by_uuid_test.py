from AllMethods.all_methods import get_news_by_uuid, validate_jsonschema


def test_get_news_by_uuid():
    response = get_news_by_uuid()
    assert response.status_code == 200


def test_jsonschema_news_by_uuid():
    schema = open("schemes/get_news_by_uuid.json").read()
    response = get_news_by_uuid()
    validate_jsonschema(schema, response)
