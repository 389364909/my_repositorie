from lxml import etree
import requests

header = {}

url = ''
string = requests.get(url,headers = header,timeout=10).text
#print(string)
html = etree.HTML(string)
xpath = html.xpath('')

for x in xpath: 
    a = etree.tostring(x,encoding='utf-8').decode('utf-8')
    print(a)

#print(xpath)


