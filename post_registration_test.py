import json
import time
import jsonschema
import pytest
import allure
from qadata import *
from Allmethods import *

password = '123456'
oldemail = 'korbit.bot@gmail.com'
newemail = 'korbit.bit+' + str(time.time()) + '@gmail.com'


@allure.step("Регистрация нового пользователя. 200 ОК и валидация json")
def test_post_registration():
    response = post_registration(email=newemail, password=password)
    assert response.status_code == 200
    schema = open("schemes/post_auth.json").read()
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            pytest.fail(error)
    except jsonschema.ValidationError as e:
        pytest.fail(e)


@allure.step("Регистрация уже зарегистрированным пользователем")
def test_registration_already_registered():
    response = post_registration(email=oldemail, password=password)
    assert response.status_code == 401

failedemail = id_generator() + '@test.com'

@allure.step("Регистрация с пустыми данными. 400 Bad request?")
def test_registration_emptydata():
    response = post_registration(email=failedemail, password=password, firstname='', lastname='')
    assert response.status_code == 400


