import json

import jsonschema
import pytest

import allure
from Allmethods import *


@allure.step("Статус код 200 ОК?")
def test_get_charity_by_uuid():
    response = get_charity_by_uuid()
    assert response.status_code == 200


@allure.step("Валидация структуры JSON и типов данных")
def test_jsonschema_charity_by_uuid():
    schema = open("schemes/get_charity_by_uuid.json").read()
    response = get_charity_by_uuid()
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            pytest.fail(error)
    except jsonschema.ValidationError as e:
        pytest.fail(e)
