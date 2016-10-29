from Allmethods import get_history

email = 'korbit.bot@gmail.com'
password = '123456'


def test_get_history():
    response = get_history(email=email, password=password)
    assert response.status_code == 200

'''
@allure.step("Валидация структуры JSON и типов данных")
def test_jsonschema_history():
    schema = open("schemes/get_history.json").read()
    response = get_history(email=email, password=password)
    try:
        v = jsonschema.Draft4Validator(json.loads(schema))
        for error in sorted(v.iter_errors(json.loads(response.text)), key=str):
            print(error.message)
    except jsonschema.ValidationError as e:
        pytest.fail(e)
'''
