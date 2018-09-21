#动漫壁纸
#http://www.netbian.com/dongman/index.htm
import requests
from lxml import etree
from contextlib import closing
import sys
import os
start = input("请输入总页数：")

headers = ""
urls = ["http://www.netbian.com/dongman/index.htm"]
for i in range(2,int(start)):
	urls.append("http://www.netbian.com/dongman/index_"+str(i)+".htm")

class ProgressBar(object):
    def __init__(self, title, count=0.0, run_status=None, fin_status=None, total=100.0,    unit='', sep='/', chunk_size=1.0):
        super(ProgressBar, self).__init__()
        self.info = "[%s] %s %.2f %s %s %.2f %s"
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or " " * len(self.statue)
        self.unit = unit
        self.seq = sep

    def __get_info(self):
        # 【名称】状态 进度 单位 分割线 总数 单位
        _info = self.info % (self.title, self.status, self.count/self.chunk_size, self.unit, self.seq, self.total/self.chunk_size, self.unit)
        return _info

    def refresh(self, count=1, status=None):
        self.count += count
        # if status is not None:
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = '\n'
            self.status = status or self.fin_status
        print(self.__get_info(), end=end_str)
        # sys.stdout.write(self.__get_info())
        sys.stdout.flush()

def getDataList(url,headers,xpath):
	r = requests.get(url,headers=headers)
	html = etree.HTML(r.text)
	lis = html.xpath(xpath)
	return lis

def main():
	for url in urls:
		lis = getDataList(url,headers,"//*[@id='main']/div[2]/ul/li/a/@href")
		for li in lis:
			downloadUrl = getDataList("http://www.netbian.com"+li,"","//*[@id='main']/div[2]/div/div/a/@href")
			for img in downloadUrl:
				links = getDataList("http://www.netbian.com"+downloadUrl[0],"","//*[@id='endimg']/tr/td/a")
				for link in links:
					title = link.xpath("@title")[0];
					src	  = link.xpath("@href")[0];
					filename = src.split("/")[-1]
				with closing(requests.get(src, stream=True)) as response:
					chunk_size =1024
					content_size = int(response.headers['content-length'])
					progress = ProgressBar(title, total=content_size, unit="KB", chunk_size=chunk_size, run_status="正在下载", fin_status="下载完成")
					# chunk_size = chunk_size &lt; content_size and chunk_size or content_size
					if os.path.exists('./图片/'+filename) and os.path.getsize('./图片/'+filename)==content_size:
						print ("图片已下载！")
					else:
						with open('./图片/'+filename, "wb") as file:
							for data in response.iter_content(chunk_size=chunk_size):
								file.write(data)
								progress.refresh(count=len(data))
					
if __name__=="__main__":
	main()