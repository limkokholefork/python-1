
#抓取地址： http://www.27270.com
import requests
from lxml import etree
import sys
url = "http://www.27270.com";
re = requests.get(url);
re.encoding = re.apparent_encoding #apparent_encoding可以获得真实编码
text = re.text;
tree = etree.HTML(text);
lists = tree.xpath("//*[@class='NenuLi']/a");
for lis in lists:
	hrefs = lis.xpath('@href')[0];
	titles = lis.xpath('text()')[0];
	print(hrefs);
