import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1106587.json"
#url = "http://py4e-data.dr-chuck.net/comments_42.xml"
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
data = data.decode()

print('Retrieved', len(data), 'characters')
items = json.loads(data)
print('Items count:', len(items))

totals = []
for item in items['comments']:

	#print(item['name'])

	try:
		#print(item['count'])
		totals.append(int(item['count']))
	except:
		#print(item)
		print("Failed to get count")
	#print('Name: ', item['name'])
	#print('Count: ', item['count'])

print(totals)
print("The sum is ", sum(totals))