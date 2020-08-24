import requests,json

url = 'http://alekseikorobov.pythonanywhere.com/version'

cfg = json.load(open('config.json','r'))

r = requests.get(url,verify=False)
if r.status_code == 200:
    if r.content == cfg['version']:
        print('all ok')
    else:
        print(r.content)
        print(cfg['version'])
else:
    print(r.content)
