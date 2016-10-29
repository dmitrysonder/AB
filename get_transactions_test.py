from Allmethods import get_transactions

email = 'korbit.bot@gmail.com'
password = '123456'


def test_get_transactions():
    response = get_transactions(email, password)
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
