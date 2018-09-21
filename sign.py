#coding=utf-8

from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains #导入鼠标操作
#from selenium.webdriver.common.keys import Keys #导入键值操作
import time
# zhanghao = [{username:'1282074911',password:'a1024800331'},{username:'946960672',password:'a1024800331'}]
username = '1282074911' #用户名
password = 'a1024800331' #密码

signpage = 'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=http://game.qq.com/comm-htdocs/milo/proxy.html&appid=21000501&target=top&s_url=http%3A%2F%2Fwuxia.qq.com%2Fcp%2Fa20180117tdspring%2F&style=20&daid=8' #签到页面

browser = webdriver.PhantomJS()
browser.get(signpage)
browser.find_element_by_xpath("//*[@id='switcher_plogin']").click()
browser.find_element_by_id("u").send_keys(username)
browser.find_element_by_id("p").send_keys(password)
browser.find_element_by_id("login_button").click()
time.sleep(10)
browser.find_element_by_xpath("//*[@id='wrapper']/div[2]/div[4]/a[1]").click()
print(browser.find_element_by_id("daysNum").text)
# daysNum 
input()
browser.quit()


