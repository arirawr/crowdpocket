import datetime
import requests
from keys import keys

# AUTH
ck = keys['consumer_key']
users = keys['group_users']

tags = ['bae']

# ACTIONS

actions = '['

for user in users:
	for tag in tags:
		payload = {'consumer_key': ck, 'access_token': user, 'tag': tag}
		r = requests.get("https://getpocket.com/v3/get", params=payload)
		if r.json()['list']:
			json_key = r.json()['list'].keys()
			for key in json_key:
				found_url = r.json()['list'][key]['given_url']
				action = '{ "action" : "add", "tags" : "' + tag + '", "url" : "' + found_url + '"},'
				actions += action
actions = actions[:-1]
actions += ']'
print datetime.datetime.now()
print actions

#actions = '[{ "action" : "add", "tags" : "' + tags + '", "url" : "' + found_url + '"}]'

#actions = '[{ "action" : "add", "tags" : "zakari", "url" : "http://google.com"},{ "action" : "add", "tags" : "zakari", "url" : "http://mcgill.ca"}]'

if actions != ']':
	for user in users:
		payload = {'consumer_key': ck, 'access_token': user, 'actions': actions}
		r = requests.post("https://getpocket.com/v3/send", params=payload)
		print r.text
else: 
	print "no actions"