# coding=utf-8
from web.webkeys import Web

webobj = Web()
# 打开谷歌浏览器
webobj.openbrowser('gc')
# 访问网站
webobj.geturl('http://112.74.191.10:8000/')
# 登录
webobj.click_link('//*[text()="登录"]')
webobj.input('//*[@id="username"]', '13800138006')
webobj.input('//*[@id="password"]', '123456')
webobj.input('//*[@id="verify_code"]', '111')
webobj.js_click('//*[@id="loginform"]/div/div[6]/a')
# 校验
webobj.sleep(2)
webobj.gettext('/html/body/div[1]/div/div/div/div[2]/a[1]')
webobj.assertequals('南京', '登录')
webobj.sleep(3)
webobj.quit()
