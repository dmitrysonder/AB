import json
import jsonschema
import pytest
from AllMethods import post_auth

email = 'korbit.bot@gmail.com'
password = '123456'
bad_pass = '1234567'


def test_post_auth():
    response = post_auth(email=email, password=password)
    assert response.status_code == 200


def test_jsonschema_auth():
    schema = open("schemes/post_auth.json").read()
    response = post_auth(email=email, password=password)
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            pytest.fail(error)
    except jsonschema.ValidationError as e:
        pytest.fail(e)


def test_auth_incorrect_passwd():
    response = post_auth(email=email, password=bad_pass)
    assert response.status_code == 401
