# coding=utf-8
from inter.interkeys import HTTP

# 创建一个http请求库的实例对象
http = HTTP()
# 设置基础url地址
http.seturl('http://112.74.191.10:80/inter/HTTP/')
http.post('auth', '')
# 保存token
http.savejson('token','token')
# 添加token到头里面
http.addheader('token', '{token}')
# 登录
http.post('login', 'username=Will4&password=123456')
# 保存userid
http.savejson('userid','userid')
# 获取用户信息
http.post('getUserInfo', 'id={userid}')
http.post('logout', None)
