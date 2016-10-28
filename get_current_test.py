import allure
from Allmethods import *

email = 'korbit.bot@gmail.com'
password = '123456'

@allure.step("Статус код 200 ОК?")
def test_get_current():
    response = get_current(email,password)
    assert response.status_code == 200


'''@allure.step("Валидация структуры JSON и типов данных")
def test_jsonschema_topmembers():
    schema = open("schemes/get_topmembers.json").read()
    response = get_topmembers()
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            pytest.fail(error)
    except jsonschema.ValidationError as e:
        pytest.fail(e)'''
