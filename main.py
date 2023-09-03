import requests
from bs4 import BeautifulSoup
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context
headers = {'User-Agent': 'Mozilla/5.0'}
url ="https://www.apple.com/tw/shop/refurbished/mac"

response = requests.get(url,headers = headers)
html = BeautifulSoup(response.text,features="html.parser")
script = html.find_all("script")
x = str(script[-3].text)
data = json.loads(x[43:-10])
result = []
for d in data['tiles']:
    result.append({'title':d['title'],'price':d['price']['currentPrice']['amount']})
for r in result:
    if r['title'].find('14 吋 MacBook Pro') != -1:
        print(r['title'])
        print(r['price'])


