# coding=utf-8
# import requests
#
# session = requests.session()
# # 添加头部校验
# """
# 'content-type'：可能影响服务器接收参数
# 'user-agent'：请求的客户端类型
# 'x-zse-83': 客户端版本号
# """
# header = {
#     'content-type': 'application/x-www-form-urlencoded',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
#     'x-zse-83':'3_2.0',
# }
# session.headers.update(header)
# # 请求udid
# result = session.post('https://www.zhihu.com/udid')
# print(result.text)
# """
# 注意：凡是在请求返回头里面有set-cookie字样的关联字段
# 使用session管理后，是不需要手动关联
# """
# print(session.cookies)
# # 获取验证码票据
# result = session.get('https://www.zhihu.com/api/v3/oauth/captcha?lang=cn')
# print(result.text)
#
# # 发送知乎登录包
# result = session.post('https://www.zhihu.com/api/v3/oauth/sign_in',
#                       data='aR79k4U0cT2tXqYq8LPG6vHmxq2pkLnmtbSBDgg9kLtxgeSmhbfGiqX1jbfVoG398LF0gQN0cT2tuqYq8LkMQbwGivwOgUxGw9e0g4e8kCV92vgBzh3qk4R92LkYFhVGwqoVJbCGST2tECx9BLkBEJXmST2tXqYhZUS8eDC8FBtxg7Fqm4O8nCL8DU3m2LPB8vSG2gC8QBtxg_VBXbP1UvLKQ_2pkLkBXgxGEJeGsgHm2LfBpwNmkveMcBtxgTtyM_OyrAL0cHFpHGFqZutqoeUq6R2YQ8Y0ZGFBe498HUFpk0NqGRt924_BkC3VUbSBtq3qk478gGpucUO1PD3ZJCe8Xq2tgqNMsvSMS79hbTFXrRFq8TFqoe9qr_LxgRVmZ9oMgGL1eBtxg_NMwGoM2JXMXq2tguVKKvwGEJHM3BtxgRF0zuFqrH9BrXxpggY8BTxyNguq6X2fS828G8OBFgr8Xq2tHgSVKbOBDBe8')
# print(result.text)


import requests
from urllib.parse import quote

session = requests.session()
session.headers['token'] = 'e1ae6bc2bb0e45ae8922fab6a3d4e4a2'
res = session.post('http://112.74.191.10:8081/inter/REST/user/register',data='%7B%22username%22%3A%22Tester%22%2C%22pwd%22%3A%22123456%22%2C%22nickname%22%3A%22%E6%B5%8B%E8%AF%95%E8%B4%A6%E5%8F%B7%22%2C%22describe%22%3A%22%E8%BF%99%E6%98%AF%E4%B8%80%E4%B8%AA%E6%B5%8B%E8%AF%95%E6%B3%A8%E5%86%8C%E7%9A%84%E8%B4%A6%E5%8F%B7%22%7D')
print(res.text)
