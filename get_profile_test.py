from AllMethods.all_methods import get_profile, validate_jsonschema

email = 'korbit.bot@gmail.com'
password = '123456'


def test_get_profile():
    response = get_profile(email=email, password=password)
    assert response.status_code == 200


def test_jsonschema_profile():
    schema = open("schemes/get_profile.json").read()
    response = get_profile(email=email, password=password)
    validate_jsonschema(schema, response)

