import requests
from lxml import etree
import re
import json
exurl = 'http://www.27270.com/game/cosplaymeitu/list_20_';
url = 'http://www.27270.com/game/cosplaymeitu/list_20_1.html';
pageJson = {};
cosJson = {};
def screen(url,xpath):
	req = requests.get(url);
	req.encoding = req.apparent_encoding;
	tree = etree.HTML(req.text);
	target = tree.xpath(xpath);
	return target;

def getCosJson(url):
	urls = [];
	pages = screen(url,'//*[@class="NewPages"]/ul/li[last()]/a/@href')[0];
	endPage = re.sub('list_(\d)+_|.html','',pages);
	for page in range(1,int(endPage)+1):
		print(page);
		pageUrl = exurl+str(page)+'.html';
		coslist = screen(pageUrl,'/html/body/div[2]/div[1]/div[8]/ul/li/a');
		pageCos =[];
		for cos in coslist:
			pageCos.append({'title':cos.get('title'),'href':cos.get('href')})
		pageJson[page] = pageCos;
	with open('cos.json','w') as f:
		json.dump(pageJson,f)
def getImages(url):
 	cos = screen(url,'body') 
 	pages = cos[0].xpath('//*[@id="pageinfo"]')[0].get('pageinfo');
 	imgsrcs = [];
 	for page in range(1,int(pages)+1):
 		imgurl = re.sub('.html','_'+str(page)+'.html',url);
 		imgSrc = screen(re.sub('.html','_'+str(page)+'.html',url),'//*[@id="picBody"]/p/a[1]/img/@src');
 		if len(imgSrc) > 0:
 			imgsrcs.append(imgSrc[0]);
 	return imgsrcs;

with open('cos.json') as f:
	data = json.load(f);
	total = 0;
	now = 1;
	print('开始抓取...')
	for index in data:
		total +=len(data[index])
	for index in data:
		dataItems = [];
		for item in data[index]:
			item['href'] = getImages(item['href']);
			print(str(now)+'/'+str(total))
			now+=1;
			dataItems.append(item);
		data[index] = dataItems;
	with open('cos_src.json',"w") as f:
		json.dump(data,f);