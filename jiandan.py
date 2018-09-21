#煎蛋网
import requests
from lxml import etree
import pymysql
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
conn = pymysql.connect(host="localhost",port=3306,user='root',password="root",db="cos",charset="utf8")
cur  = conn.cursor()
# item = "sdfs"
# result = cur.execute("insert into cos_img (link,test) values (%s,%s)",(item,"test"))
# conn.commit()
# print(result)
# exit()
#http://jandan.net/ooxx/page-503#comments
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
#利用PhantomJS加载网页
browser = webdriver.PhantomJS()
browser.set_page_load_timeout(30) # 最大等待时间为30s
#当加载时间超过30秒后，自动停止加载该页面
def getImgs(url):
	data = [];
	try:
	    browser.get(url)
	except Exception as e:
		#browser.quit()#退出页面
		print('加载失败')
		return
	source = browser.page_source #获取网页源代码
	#browser.quit()#退出页面
	html = etree.HTML(source)
	lis = html.xpath("//ol/li")
	for li in lis:
		try:
			link = li.xpath("div/div/div[2]/p/img/@src")[0]
			code = li.xpath("@id")[0].split("-")[1]
		except Exception as e:
			continue
		data.append({'link':link,'code':code})
	return data

for x in range(1,504):
	print("正在加载第"+str(x)+"页....")
	data = getImgs('http://jandan.net/ooxx/page-'+str(x))
	if not data:
		continue
	for item in data:
		cur.execute('insert into jd_img (link,code) values (%s,%s)',(item['link'],item['code']))
		conn.commit()
		#print(conn.insert_id())
	#time.sleep(5)	
input("加载完毕!")