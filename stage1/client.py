import requests

def get_balance():
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    print(r.json())
    return r.status_code