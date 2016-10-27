import json
import jsonschema
from Allmethods import *
import pytest
import allure


@allure.step("Статус код 200 ОК?")
def test_get_news_by_uuid():
    response = get_news_by_uuid()
    assert response.status_code == 200


@allure.step("Валидация структуры JSON и типов данных")
def test_jsonschema_news_by_uuid():
    schema = open("schemes/get_news_by_uuid.json").read()
    response = get_news_by_uuid()
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            pytest.fail(error)
    except jsonschema.ValidationError as e:
        pytest.fail(e)
