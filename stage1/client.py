import requests

URL = 'http://localhost'
PORT = 5000

def get_balance():
    payload = {
        'user':'xu'
    }
    r = requests.get('{}:{}/balance'.format(URL,PORT),params=payload)
    print(r.text)
    return r.status_code

def create_user(user):
    to_add_user = {'user':user}
    r = requests.post('{}:{}/user'.format(URL,PORT),json=to_add_user)
    print(r.url)
    return r.status_code