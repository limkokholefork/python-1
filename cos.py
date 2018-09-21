#Cosplay
import requests
from lxml import etree
import time
import sys
import json
import pymysql

conn = pymysql.connect(host='localhost',port=3306,user='root',password='root',db="cos",charset="utf8")
cur  = conn.cursor()

def getDetailUrl(url,headers):
	detail_urls = []
	r = requests.get(url,headers = headers)#,timeout=5000 设置超时时间
	#获取html页面内容
	html = etree.HTML(r.text)
	# print(url)
	#通过xpath规则初步获取
	lis = html.xpath("/html/body/div[@class='box']/div[@class='pics']/ul/li")
	# print(len(lis))
	for li in lis:	
		try:
			title = li.xpath("p[1]/a/text()")[0]
		except Exception as e:
			title = "未知"
		try:
			author= li.xpath("p[2]/a/text()")[0]
		except Exception as e:
			author = "未知"
		links = "http://cosplay.la"+li.xpath("a/@href")[0]
		code  = links.split("/")[-1]
		cover = li.xpath("a/img/@src")[0]
		detail_urls.append({'title':title,'links':links,'coser':author,'cover':cover,'code':code})
	return detail_urls

def getDetailHtml(url,headers):
	r = requests.get(url,headers = headers)
	html = etree.HTML(r.text)
	# title = str(html.xpath("//h1/text()")[0])+"@"+str(authon)
	stites  = html.xpath("//div['talk_pic']/p[@class='mbottom10']/a/img/@src")
	return stites


urls = []
headers = {}
datas = []
for x in range(1,232,1):
	pages ={}
	pages["page"] = x
	pages["data"] = []
	print("-------------------正在加载第"+str(x)+"页-------------------")
	data = getDetailUrl("http://cosplay.la/photo/index/0-1-"+str(x),headers)
	length = str(len(data))
	now = 1
	# print(length)
	for item in data:
		print(str(now)+"/"+length)
		item["links"]=getDetailHtml(item["links"],headers)
		num = len(item["links"])
		try:
			cur.execute("insert into cos_list (code,title,coser,num,cover)  values (%s,%s,%s,%s,%s)" ,(item['code'],item['title'],item['coser'],str(num),item['cover']))
		except Exception as e:
			print("加载失败1")
			continue
		pid = int(conn.insert_id())
		for link in item['links']:
			try:
				cur.execute("insert into cos_links (link,pid) values (%s,%s)",(link,pid))
			except Exception as e:
				print("加载失败")
				continue

		pages["data"].append(item)
		# datas.append()
		now += 1
		datas.append(pages)
	print("-------------------第"+str(x)+"页加载完成-------------------")

# filename = "F:/迅雷下载/图片/cos201-228.json"
# with open(filename,"w",encoding='utf-8') as file_obj:
# 	json.dump(datas,file_obj,ensure_ascii=False)
input("爬取完成，按回车键退出")