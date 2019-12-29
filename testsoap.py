# coding=utf-8
from suds.client import Client
import json


# 创建强求webservice的客户端
client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl')
# 使用客户端调服务器的接口
res = client.service.__getattr__('auth')()
headers = {}
headers['token'] = json.loads(res)['token']
# 创建强求webservice的客户端
client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl',headers=headers)

params = ['Will','123456']
res = client.service.login(*params)
print(res)
client.service.logout()





