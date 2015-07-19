import datetime
import requests
from keys import keys, userkeys, groups

# App key
ck = keys['consumer_key']

def update(groupname):

	group = groups[groupname]
	members = group['members']
	tags = group['tags']

	# ACTIONS
	
	actions = '['
	
	for member in members:
		for tag in tags:
			payload = {'consumer_key': ck, 'access_token': userkeys[member], 'tag': tag}
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
	
	if actions != ']':
		for member in members:
			payload = {'consumer_key': ck, 'access_token': userkeys[member], 'actions': actions}
			r = requests.post("https://getpocket.com/v3/send", params=payload)
			print r.text
	else: 
		print "no actions"
		
for group in groups:
	update(group)