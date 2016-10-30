from AllMethods.all_methods import get_news, validate_jsonschema


def test_get_news():
    response = get_news()
    assert response.status_code == 200


def test_jsonschema_news():
    schema = open("schemes/get_news.json").read()
    response = get_news()
    validate_jsonschema(schema, response)
