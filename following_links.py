# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

choice = input('Would you like the sample or the actual? ')
if choice.lower() == 'sample':
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
    position = 2
    repeat = 4
else:
    url = 'http://py4e-data.dr-chuck.net/known_by_Dex.html'
    position = 17
    repeat = 7

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

print(url)
for x in range(repeat):
    print(tags[position])
    url = str(tags[position])
    start = url.find('http')
    stop = url.find('html')
    url = url[start:stop + 4]
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')




    
