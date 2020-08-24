#https://www.pythonanywhere.com/user/alekseikorobov/account/#api_token
#https://help.pythonanywhere.com/pages/API


import requests
import json

cfg = json.load(open("config_private.json", "r"))

username = cfg['username']
token = cfg['token']
domain_name = 'alekseikorobov.pythonanywhere.com'
command = 'consoles'

baseUrl = 'https://www.pythonanywhere.com/api/v0/user/{username}/{command}/'
commandUrl = 'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{id}/send_input/'
get_latest_output_url = 'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{id}/get_latest_output/'
reload_command_url = 'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'

print('get console....')
response = requests.get(
  baseUrl.format(
      username=username,
      command=command
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)},
  verify=False
)
if response.status_code == 200:  
  bytes = response.content
  str = bytes.decode("utf-8")
  list = eval(str)
  #print(list)
  if len(list)>0:
    id = list[0]['id']
    print(id)
  else:
    print('create new console')
    pass

  print('git pull...')
  data={'input':'git pull\n'}
  response = requests.post(
    commandUrl.format(
        username=username,
        id=id
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)},
    data=data,
    verify=False
  )
  print(response.status_code)
  print(response.content)

  print('reload ... ')

  response = requests.post(
    reload_command_url.format(
        username=username,
        domain_name=domain_name
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)},
    verify=False
  )
  print(response.status_code)
  print(response.content)

  # if response.status_code ==200:
  #   response = requests.get(
  #     get_latest_output_url.format(
  #         username=username,
  #         id=id
  #     ),
  #     headers={'Authorization': 'Token {token}'.format(token=token)}
  #   )
  #   print(response.status_code)
  #   print(response.content)


else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))