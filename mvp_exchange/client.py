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
    return r.status_code

def transfer_money(from_who, to, amount):
    transfer_info = {
        'from_who':from_who,
        'to':to,
        'amount':amount}
    r = requests.post('{}:{}/transfer'.format(URL,PORT),json=transfer_info)
    return r.status_code
