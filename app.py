import requests
from keys import keys

# AUTH
ck = keys['consumer_key']
at = keys['access_token']

# ACTIONS
actions = [
	{
		"action" : "add",
		"item_id" : "89419281",
	}
]

payload = {'consumer_key': ck, 'access_token': at, 'actions': actions}
r = requests.post("https://getpocket.com/v3/send", params=payload)