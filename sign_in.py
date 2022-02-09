
import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

login_data = {
    'name': 'squale96',
    'pass': 'Alesqu96!',
    'form_id': 'new_login_form',
    'op': 'Login'
}

with requests.Session() as s:
    url = 'https://www.codechef.com/'
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    login_data['form_build_id'] = soup.find('input', attrs={'name': 'form_build_id'})['value']
    r = s.post(url, data=login_data, headers=headers)
    print(r.content)
