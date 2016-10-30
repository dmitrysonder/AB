from AllMethods.all_methods import post_photo, validate_jsonschema

email = 'korbit.bot@gmail.com'
password = '123456'
with open("base64_image.txt") as file:
    image = file.read()
    file.close()


def test_post_photo():
    response = post_photo(email=email, password=password, image=image)
    assert response.status_code == 200


def test_jsonschema_photo():
    schema = open("schemes/get_profile.json").read()
    response = post_photo(email=email, password=password, image=image)
    validate_jsonschema(schema, response)

print(image)

