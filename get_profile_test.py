import json

import jsonschema
import pytest

import allure
from Allmethods import *

email = 'korbit.bot@gmail.com'
password = '123456'

@allure.step("Статус код 200 ОК?")
def test_get_profile():
    response = get_profile(email=email, password=password)
    assert response.status_code == 200

@allure.step("Валидация структуры JSON и типов данных")
def test_jsonschema_profile():
    schema = open("schemes/get_profile.json").read()
    response = get_profile(email=email, password=password)
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            print(error.message)
    except jsonschema.ValidationError as e:
        pytest.fail(e)
