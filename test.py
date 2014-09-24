#!/Python34/python
# -*- coding: utf-8 -*-
import sys
import json
import cgi
from bs4 import BeautifulSoup as bs
from urllib3 import PoolManager

fs = cgi.FieldStorage()
pm = PoolManager(1)


sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

result = {}
result['success'] = True
result['message'] = "The command Completed Successfully"
result['keys'] = ",".join(fs.keys())

d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

result['data'] = d

if not d.get('url'):
    url = "http://clickshop.hu/bosch-psb-450-uetvefuro--18323/"
else:
    url = d['url']

productsite = pm.request('GET', url)
sitedata = productsite.data
soup = bs(sitedata)

productName = soup.h1.string.rstrip().lstrip()
productImageUrl = "test.png"

result['productName'] = productName
productPrice = soup.find('span', {'class' : 'price'}).text
#print(productPrice)
#productPrice = productPrice.string
productPrice = productPrice.replace(u"\u00A0", " ")
result['productPrice'] = productPrice
result['productImageUrl'] = productImageUrl

#result['message2'] = "this too:" + d['url']

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()


