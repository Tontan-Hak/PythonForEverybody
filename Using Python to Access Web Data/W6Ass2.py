import urllib.parse as up
import urllib.request as ur
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?key=42&'

place_name = input("Enter Location: ")
params = {"sensor": "false", "address": place_name}  # Fix the variable name to 'place_name'
url = serviceurl + up.urlencode(params)
print("Retrieving ", url)
data = ur.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

place_id = json_obj['results'][0]['place_id']
print('Place Id: ', place_id)
