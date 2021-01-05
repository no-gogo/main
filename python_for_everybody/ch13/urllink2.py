# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1106584.html"
try:
	html = urlopen(url, context=ctx).read()
except:
	print("Failure in using urlopen.")
	exit()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup.find_all('span')


numbers = []

for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)

    number = tag.contents[0]
    numbers.append(number)

print(numbers)

for i in range(0, len(numbers)): 
    numbers[i] = int(numbers[i]) 

total = sum(numbers)
print("Total:", total)