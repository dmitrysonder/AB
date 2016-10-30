import time
from AllMethods.all_methods import post_registration, validate_jsonschema
from qa_data import id_generator

password = '123456'
old_email = 'korbit.bot@gmail.com'
new_email = 'korbit.bit+' + str(time.time()) + '@gmail.com'
failed_email = id_generator() + '@test.com'


def test_post_registration():
    response = post_registration(email=new_email, password=password)
    assert response.status_code == 200
    schema = open("schemes/post_auth.json").read()
    validate_jsonschema(schema, response)


def test_registration_already_registered():
    response = post_registration(email=old_email, password=password)
    assert response.status_code == 401


def test_registration_emptydata():
    response = post_registration(email=failed_email, password=password, firstname='', lastname='')
    assert response.status_code == 400
