from AllMethods.all_methods import post_auth, validate_jsonschema

email = 'korbit.bot@gmail.com'
password = '123456'
bad_pass = '1234567'


def test_post_auth():
    response = post_auth(email=email, password=password)
    assert response.status_code == 200


def test_jsonschema_auth():
    schema = open("schemes/post_auth.json").read()
    response = post_auth(email=email, password=password)
    validate_jsonschema(schema, response)


def test_auth_incorrect_password():
    response = post_auth(email=email, password=bad_pass)
    assert response.status_code == 401
