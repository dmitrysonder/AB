from AllMethods.all_methods import get_history

email = 'korbit.bot@gmail.com'
password = '123456'


def test_get_history():
    response = get_history(email=email, password=password)
    assert response.status_code == 200


'''
def test_jsonschema_history():
    schema = open("schemes/get_history.json").read()
    response = get_history(email=email, password=password)
    validate_jsonschema(schema, response)
'''
