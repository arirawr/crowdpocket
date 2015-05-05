import requests
from keys import keys

# AUTH
ck = keys['consumer_key']
at = keys['access_token']
ari = keys['ari']
zak = keys['zak']

payload = {'consumer_key': ck, 'redirect_uri': 'http://ariari.io'}
r = requests.post("https://getpocket.com/v3/oauth/request", params=payload)
print r.text