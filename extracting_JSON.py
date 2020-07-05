import urllib.request, urllib.parse, urllib.error
import json
import ssl

choice = input('Would you like the sample or the actual? ')
if choice.lower() == 'sample':
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
else:
    url = 'http://py4e-data.dr-chuck.net/comments_703191.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    print('Explode')

#print(json.dumps(js['comments']))

total = 0

for item in js['comments']:
    total += int(item['count'])

print(total)