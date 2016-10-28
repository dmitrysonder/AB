import json
import jsonschema
import pytest
import allure
from AllMethods import *

email = 'korbit.bot@gmail.com'
password = '123456'
badpass = '1234567'

@allure.step("Статус код 200 ОК?")
def test_post_auth():
    response = post_auth(email=email, password=password)
    assert response.status_code == 200

@allure.step("Валидация структуры JSON и типов данных")
def test_jsonschema_auth():
    schema = open("schemes/post_auth.json").read()
    response = post_auth(email=email, password=password)
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            pytest.fail(error)
    except jsonschema.ValidationError as e:
        pytest.fail(e)

@allure.step("Авторизация с неверным паролем")
def test_auth_incorrect_passwd():
    response = post_auth(email=email, password=badpass)
    assert response.status_code == 401





