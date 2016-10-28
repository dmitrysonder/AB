import requests

BASE_URL = 'http://appybuy.korbit.eu:8080/magnoliaPublic/.rest/appybuy/v1'

def get_charities(count=200, start=0, sort='richest', lang='eng', filter='', search='', alphabet='', confirmed=True):
    payload = {'count': count, 'start': start, 'sort': sort, 'lang': lang, 'filter': filter, 'search': search,
               'alphabet': alphabet, 'confirmed': confirmed}
    r = requests.get(BASE_URL + '/charities', params=payload)
    return r

def get_charity_by_uuid(uuid='1e7e3073-fa53-4919-a48a-16d209974dcd', lang='eng'):
    payload = {'lang':lang}
    r = requests.get(BASE_URL + '/charity/' + uuid, params=payload)
    return r

def get_categories(lang='eng'):
    payload = {'lang':lang}
    r = requests.get(BASE_URL + '/charities/categories', params=payload)
    return r

def get_topmembers(uuid='1e7e3073-fa53-4919-a48a-16d209974dcd'):
    payload = {'uuid':uuid}
    r = requests.get(BASE_URL +'/charities/topmembers', params=payload)
    return r

def get_news(filter='', uuid='', count=200, start=2, lang='de'):
    payload = {'uuid': uuid, 'filter':filter, 'count':count, 'start':start, 'lang':lang}
    r = requests.get(BASE_URL +'/news', params=payload)
    return r

def get_news_by_uuid(uuid='6d6737c3-886e-4f44-a5ad-6721bac3a659', lang='eng'):
    payload = {'lang':lang}
    r = requests.get(BASE_URL + '/news/' + uuid, params=payload)
    return r

def post_registration(email,password,firstname='APITESTER',lastname='DEFAULT',birthdate='1991-07-04',sex='1'):
    payload = {'email':email, 'password':password, 'firstname':firstname, 'lastname':lastname, 'birthdate':birthdate, 'sex':sex}
    headers = {'Content-Type':'application/json'}
    r = requests.post(BASE_URL + '/member/registration', json=payload, headers=headers)
    return r

def post_auth(email,password):
    headers = {'Content-type':'application/json'}
    r = requests.post(BASE_URL + '/member/auth', headers=headers, auth=(email,password))
    return r

#json=payload прочитал в доке. должно работать как json в теле пост запроса. надо проверить
def post_member_update(email, password, newemail, newpassword, firstname,lastname,birthdate,sex='0'):
    payload = {'email':newemail, 'password':newpassword, 'firstname':firstname, 'lastname':lastname, 'birthdate':birthdate, 'sex':sex}
    headers = {'Content-type': 'application/json'}
    r = requests.post(BASE_URL + '/member/update', auth=(email,password), json=payload, headers=headers )
    return r

def get_profile(email,password):
    headers = {'Content-type': 'application/json'}
    r = requests.get(BASE_URL + '/member/profile', auth=(email,password), headers=headers)
    return r

def get_transactions(email,password):
    headers = {'Content-type': 'application/json'}
    r = requests.get(BASE_URL + '/member/transactions', auth=(email, password), headers=headers)
    return r

def get_current(email, password):
    headers = {'Content-type': 'application/json'}
    r = requests.get(BASE_URL + '/member/current', auth=(email, password), headers=headers)
    return r

#uuid of charity, that you want to make active
def post_current(email,password,uuid):
    payload = {'uuid':uuid}
    headers = {'Content-type': 'application/json'}
    r = requests.post(BASE_URL + '/member/update', auth=(email,password), json=payload, headers=headers )
    return r

def get_history(email, password):
    headers = {'Content-type': 'application/json'}
    r = requests.get(BASE_URL + '/member/history', auth=(email, password), headers=headers)
    return r

#image нужно вставлять data:image/gif;base64,R0lGODl....
def post_photo(email,password,image):
    payload = {'image':image}
    headers = {'Content-type': 'application/json'}
    r = requests.post(BASE_URL + '/member/update', auth=(email,password), json=payload, headers=headers )
    return r











