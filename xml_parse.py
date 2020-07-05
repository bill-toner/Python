#  Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_703190.xml (Sum ends with 69)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


selection = input('Would you like the sample or the actual? ')
if selection.lower() == 'sample':
    address = 'http://py4e-data.dr-chuck.net/comments_42.xml'
else:
    address = 'http://py4e-data.dr-chuck.net/comments_703190.xml'

parms = dict()
parms['address'] = address
#if api_key is not False: parms['key'] = api_key
url = address # + urllib.parse.urlencode(parms)
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
sum = 0
for count in counts:
    sum += int(count.find('count').text)
print(sum)

