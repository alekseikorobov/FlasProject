#https://www.pythonanywhere.com/user/alekseikorobov/account/#api_token


import requests

cfg = json.load(open("config.json", "r"))

username = cfg['username']
token = cfg['token']

response = requests.get(
  'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
      username=username
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('CPU quota info:')
  print(response.content)
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))