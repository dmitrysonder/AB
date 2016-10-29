import json
import jsonschema
import pytest
from Allmethods import get_categories


def test_get_categories():
    response = get_categories()
    assert response.status_code == 200


def test_jsonschema_categories():
    schema = open("schemes/get_categories.json").read()
    response = get_categories()
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            pytest.fail(error)
    except jsonschema.ValidationError as e:
        pytest.fail(e)
