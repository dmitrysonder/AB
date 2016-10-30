from AllMethods.all_methods import get_current

email = 'korbit.bot@gmail.com'
password = '123456'


def test_get_current():
    response = get_current(email, password)
    assert response.status_code == 200


'''
def test_jsonschema_topmembers():
    schema = open("schemes/get_topmembers.json").read()
    response = get_topmembers()
    validate_jsonschema(schema, response)
'''
