import requests
from lxml import etree
import pymysql
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
import sys
from time import strftime,gmtime
conn = pymysql.connect(host="localhost",port=3306,user='root',password="root",db="cos",charset="utf8")
cur  = conn.cursor()
cur.execute("select max(code) from jd_img")
zuixin = cur.fetchall()[0][0]
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
r = requests.get("http://jandan.net/ooxx/",headers=headers)#,timeout=5000 设置超时时间
updateNum = 0
#获取html页面内容
html = etree.HTML(r.text)
maxpage = html.xpath("//*[@id='comments']/div[2]/div/span/text()")[0].split("[")[1].split("]")[0]
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

for x in range(int(maxpage),0,-1):
	print("正在加载第"+str(x)+"页....")
	data = getImgs('http://jandan.net/ooxx/page-'+str(x))
	if not data:
		continue
	for item in data:
		print(str(item["code"]))
		if int(item['code'])<=int(zuixin):
			if int(updateNum)>0:
				with open('jiandan.ini',"a",encoding='utf-8') as file_obj:
					file_obj.write(str(updateNum)+"           "+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"\n")
			print("更新完成！")
			browser.quit()
			sys.exit()
		src = item['link'].replace("thumb180","mw1024")
		cur.execute('insert into jd_img (link,code) values (%s,%s)',(src,item['code']))
		conn.commit()
		updateNum += 1
		#print(conn.insert_id())
	#time.sleep(5)	
input("加载完毕!")