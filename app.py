import requests
from keys import keys

# AUTH
ck = keys['consumer_key']
at = keys['access_token']
at2 = keys['at2']

tags = "example"

# ACTIONS

payload = {'consumer_key': ck, 'access_token': at2, 'tag': tags}
r = requests.get("https://getpocket.com/v3/get", params=payload)
json_key = r.json()['list'].keys()[0]
found_url = r.json()['list'][json_key]['given_url']
print found_url

actions = '[{ "action" : "add", "tags" : "' + tags + '", "url" : "' + found_url + '"}]'

payload = {'consumer_key': ck, 'access_token': at, 'actions': actions}
r = requests.post("https://getpocket.com/v3/send", params=payload)
print r.text