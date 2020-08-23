import requests,json

url = 'http://alekseikorobov.pythonanywhere.com/version'

cfg = json.load(open('config.json','r'))

r = requests.get(url)
print(r.status_code)
print(r.content)
print(cfg['version'])
