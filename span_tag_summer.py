
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

choice = input('Would you like the sample of the actual? ')
if choice.lower() == 'sample':
    url = 'http://py4e-data.dr-chuck.net/comments_42.html'
else:
    url = 'http://py4e-data.dr-chuck.net/comments_703188.html'

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
lst = []
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    tag = str(tag)
    lst.append(tag)


nums = []
for line in lst:
    nums.append(re.findall('[0-9]+', line))

total = 0
for num in nums:
    for nummy in num:
        total += int(nummy)

print(total)
    
