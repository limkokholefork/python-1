import requests,re
def bwzy_pc(value):  #传进来的这个值是要搜索影视名
    url="http://www.baiwanzy.com/index.php?m=vod-search"
    data={'wd':value,'submit':'search'}
    headers={'Referer':'http://www.baiwanzy.com/index.php?m=vod-search','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    try:
        req=requests.post(url=url,data=data,headers=headers).text   #以post提交数据
        re_url=re.findall('<div class="xing_vb">.*?<ul>.*?<li>.*?<a href="(.*?)".*?</ul>.*?</div>',req,re.S)[0]  #比配搜索到的第一个链接
        url_b='http://www.baiwanzy.com'
        if(re_url==url_b):
            return ('嗷，居然没有找到！')   #如果没有搜索结果则返回这个
        else:
            url_2=url_b+re_url     #拼接第二个URL
            req_url_2=requests.get(url_2).text    #以get的方式请求源码
            re_pm=re.findall('<div class="vodh">.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>',req_url_2,re.S)[0]   #比配片名
            re_lj=re.findall('<div class="vodplayinfo">.*?<ul>(.*?)</ul>.*?</div>',req_url_2,re.S)[0]  #比配播放链接
            re_lj=re_lj.strip()  #去掉中前后的空白符
            re_mb=re.findall('<li>.*?/>(.*?)</li>',re_lj,re.S)   #对数据进行最后的清洗
            return re_mb
    except:return '啥？出现未知错误。'    #当爬虫出现错误时返回这个