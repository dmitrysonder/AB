import json
import jsonschema
import pytest
from Allmethods import get_charities


def test_get_charities():
    response = get_charities()
    assert response.status_code == 200


def test_jsonschema_charities():
    schema = open("schemes/get_charities.json").read()
    response = get_charities()
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            pytest.fail(error)
    except jsonschema.ValidationError as e:
        pytest.fail(e)
