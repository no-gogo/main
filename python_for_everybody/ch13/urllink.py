import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Go to the html file that is linked to from the name in the position passed into function.
def follow_name(url,index):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	print(tags[index].contents[0])
	names.append(print(tags[index].contents[0]))
	#stall = input("Press Enter...")

	print(tags[index].get('href', None))
	return tags[index].get('href', None)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Start with this url
url = "http://py4e-data.dr-chuck.net/known_by_Nairn.html"


# We want to end up with names
names = []
count = 7
index = 17

# Follow the name
new_name_url = follow_name(url,index)
for x in range(1,count):
	new_name_url = follow_name(new_name_url,index)