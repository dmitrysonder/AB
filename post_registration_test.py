import json
import time
import jsonschema
import pytest
from qadata import id_generator
from Allmethods import post_registration

password = '123456'
old_email = 'korbit.bot@gmail.com'
new_email = 'korbit.bit+' + str(time.time()) + '@gmail.com'


def test_post_registration():
    response = post_registration(email=new_email, password=password)
    assert response.status_code == 200
    schema = open("schemes/post_auth.json").read()
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            pytest.fail(error)
    except jsonschema.ValidationError as e:
        pytest.fail(e)


def test_registration_already_registered():
    response = post_registration(email=old_email, password=password)
    assert response.status_code == 401

failed_email = id_generator() + '@test.com'


def test_registration_emptydata():
    response = post_registration(email=failed_email, password=password, firstname='', lastname='')
    assert response.status_code == 400
