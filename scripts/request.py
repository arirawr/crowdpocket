import requests
from keys import keys

# AUTH
ck = keys['consumer_key']
at = keys['access_token']
ari = keys['ari']

tags = "zakari2"

# ACTIONS

actions = '['

payload = {'consumer_key': ck, 'access_token': ari, 'tag': tags}
r = requests.get("https://getpocket.com/v3/get", params=payload)
json_key = r.json()['list'].keys()
for key in json_key:
	found_url = r.json()['list'][key]['given_url']
	action = '{ "action" : "add", "tags" : "' + tags + '", "url" : "' + found_url + '"},'
	actions += action
actions = actions[:-1]
actions += ']'
print actions

#actions = '[{ "action" : "add", "tags" : "' + tags + '", "url" : "' + found_url + '"}]'

#actions = '[{ "action" : "add", "tags" : "zakari", "url" : "http://google.com"},{ "action" : "add", "tags" : "zakari", "url" : "http://mcgill.ca"}]'

payload = {'consumer_key': ck, 'access_token': at, 'actions': actions}
r = requests.post("https://getpocket.com/v3/send", params=payload)
print r.text

payload = {'consumer_key': ck, 'access_token': at, 'tag': tags}
r = requests.get("https://getpocket.com/v3/get", params=payload)
json_key = r.json()['list'].keys()
for key in json_key:
	found_url = r.json()['list'][key]['given_url']
	action = '{ "action" : "add", "tags" : "' + tags + '", "url" : "' + found_url + '"},'
	actions += action
actions = actions[:-1]
actions += ']'
print actions

actions = '[{ "action" : "add", "tags" : "' + tags + '", "url" : "' + found_url + '"}]'

payload = {'consumer_key': ck, 'access_token': ari, 'actions': actions}
r = requests.post("https://getpocket.com/v3/send", params=payload)
print r.text