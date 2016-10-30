import json
import jsonschema
import pytest
from Allmethods import get_news


def test_get_news():
    response = get_news()
    assert response.status_code == 200


def test_jsonschema_news():
    schema = open("schemes/get_news.json").read()
    response = get_news()
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            pytest.fail(error)
    except jsonschema.ValidationError as e:
        pytest.fail(e)
