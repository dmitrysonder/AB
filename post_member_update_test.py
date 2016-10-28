import json
import jsonschema
import pytest
import allure
from Allmethods import *
import time
from qadata import *

email = 'userforupdate@test.com'
password = '123456'


@allure.step("Обновление email пользователя")
def test_email_update():
    newemail = 'update' + str(time.time()) + '@test.com'
    response = post_member_update(email=email, password=password, newemail=newemail)
    assert response.status_code == 200
    schema = open("schemes/get_profile.json").read()
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            pytest.fail(error)
    except jsonschema.ValidationError as e:
        pytest.fail(e)
    j = json.loads(response.text)
    assert j['email'] == newemail

@allure.step("Обновление имени и фамилии пользователя")
def test_name_update():
    firstname = id_generator(size=10)
    lastname = id_generator(size=10)
    response = post_member_update(email=email, password=password, firstname=firstname, lastname=lastname)
    assert response.status_code == 200
    schema = open("schemes/get_profile.json").read()
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            pytest.fail(error)
    except jsonschema.ValidationError as e:
        pytest.fail(e)
    j = json.loads(response.text)
    assert j['firstName'] == firstname
    assert j['lastName'] == lastname

@allure.step("Обновление пола пользователя")
def test_sex_update():
    sexvars = ['0','1','2']
    sex = random.choice(sexvars)
    response = post_member_update(email=email, password=password, sex=sex)
    assert response.status_code == 200
    schema = open("schemes/get_profile.json").read()
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            pytest.fail(error)
    except jsonschema.ValidationError as e:
        pytest.fail(e)
    j = json.loads(response.text)
    assert j['sex'] == sex






