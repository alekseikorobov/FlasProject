


import requests
from bs4 import BeautifulSoup
import json


cfg = json.load(open("config_private.json", "r"))

url='https://www.pythonanywhere.com/login/?next=/'
url2='https://www.pythonanywhere.com/user/alekseikorobov/webapps/'
url3='https://www.pythonanywhere.com/user/alekseikorobov/webapps/alekseikorobov.pythonanywhere.com/extend'

s = requests.Session()
r = s.get(url,verify=False)

print(r.status_code)
# print('-----------------------------')
# #print(r.content)

soup = BeautifulSoup(r.content,'lxml')
el = soup.find('input',{'name':'csrfmiddlewaretoken'})
token = el['value']
print(token)
data={'csrfmiddlewaretoken':token,'auth-username':cfg['username'],'auth-password':cfg['password'],'login_view-current_step':'auth'}
r = s.post(url,verify=False,data=data, headers={"Referer": url})
print(r.status_code)
#print(r.content)

r = s.get(url2,verify=False)

print(r.status_code)

soup = BeautifulSoup(r.content,'lxml')
el = soup.find('input',{'name':'csrfmiddlewaretoken'})
token = el['value']
print(token)

data={'csrfmiddlewaretoken':token}
r = s.post(url3,verify=False, headers={"Referer": url},data=data)

print(r.status_code)
print(r.content)
