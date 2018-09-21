#coding:utf-8
# -*- coding: utf-8 -*-
import requests
from lxml import etree
import os
import re

#忽略警告 https请求设置verify=False时 有时候会报错 设置这条语句可以解决
requests.packages.urllib3.disable_warnings()
note_url = "http://b.faloo.com/html/338/338393/";
html = requests.get(note_url);#获取HTML对象
html.encoding = html.apparent_encoding; #把文字编码变成页面真实的编码
text = html.text; #html文本
tree = etree.HTML(text); #将HTML文本转换成tree
table = tree.xpath("//div[@class='ni_list']/table[2]/tbody/tr/td/a/@href");
print(table);