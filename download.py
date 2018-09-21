import requests

url = "https://static.oschina.net/uploads/space/2018/0124/212222_LkxI_1428332.jpg"
file_name = url.split('/')[-1]


def download1():
    with open(file_name, mode='wb+') as f:
        f.write(requests.get(url).content)


url = "http://f004.bai.com/data/uploads/2013/0315/10/1363314292740038.jpg"
file_name = url.split('/')[-1]


def download2():
    # 使用流下载大型文件
    r = requests.get(url, stream=True)
    with open(file_name, mode='wb+') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)


download2()

url = "http://img1.3lian.com/img013/v3/74/d/41.jpg"
file_name = url.split('/')[-1]
from urllib.request import urlretrieve


def download3():
    # 返回一个元组，文件路径和 ('41.jpg', <http.client.HTTPMessage object at 0x000001EC87FC8128>)
    # Returns a tuple containing the path to the newly created
    # data file as well as the resulting HTTPMessage object.
    res = urlretrieve(url, file_name)
    print(res)


download3()