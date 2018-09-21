#https://www.80s.tw/movie/22692
import ssl
import requests
from lxml import etree
# import pymysql 
# import sys
# import json
import time
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings() 
# conn = pymysql.connect(host="localhost",port=3306,user="root",password="root",db="80s",charset='utf8')
# cur = conn.cursor()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

# https://www.80s.tw/movie/list/-----p3
r = requests.get("https://www.80s.tw/movie/list",headers,verify=False)
html = etree.HTML(r.text)
pageNum = html.xpath("//*[@class='pager']/a/@href")[-1].split("-----p")[-1]
# print(last)
# score = html.xpath("//*[@class='me1 clearfix']/li/a/span/text()") #评分
# href = html.xpath("//*[@class='me1 clearfix']/li/a/@href") #链接
# title = html.xpath("//*[@class='me1 clearfix']/li/h3/a/text()") #标题
# detail = html.xpath("//*[@class='me1 clearfix']/li/span/text()") #简介

def getMovieList(url):
	r = requests.get(url,verify=False)
	html = etree.HTML(r.text)
	lis = html.xpath("//*[@id='myform']/ul/li[not(@clsass='nohover')]");
	return lis;

def getMovieDetail(url):
	lis = getMovieList(url)
	for li in lis:
		score 	= li.xpath("span[1]/input/@value") #普通链接
		href 	= li.xpath("span[2]/a/@href") #迅雷迅雷
		# try:
		# 	mid = href[0].split("/")[-1]
		# 	cur.execute("INSERT INTO   movie (id,title,detail,cover,href,score) VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE title=%s,detail=%s,cover=%s,href=%s,score=%s",(mid,title,detail,img,href,score,title,detail,img,href,score));
		# except Exception as e:
		# 	print(e);
		print();
		print(score);
		print(href);
# for i in range(1,int(pageNum)+1):
# 	print("正在加载第"+str(i)+"页") #到84
# 	getMovieDetail("https://www.80s.tw/movie/list/-----p"+str(i))
print(getMovieDetail("https://www.80s.tw/ju/22691"));