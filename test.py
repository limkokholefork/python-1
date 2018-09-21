import requests
from lxml import etree

re = requests.get('https://www.gavbus166.com');
txt = re.text;
print(txt);
input();