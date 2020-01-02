# coding=utf-8
from suds.client import Client
import json


# # 创建请求webservice的客户端
# client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl')
# # 使用客户端调服务器的接口
# res = client.service.__getattr__('auth')()
# headers = {}
# headers['token'] = json.loads(res)['token']
# # 创建强求webservice的客户端
# client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl',headers=headers)
# 
# params = ['Will','123456']
# res = client.service.login(*params)
# print(res)
# client.service.logout()


# 天气接口

# 添加命名空间
from suds.xsd.doctor import Import, ImportDoctor

Imp = Import('http://www.w3.org/2001/XMLSchema')
Imp.filter.add('http://WebXml.com.cn/')
doctor = ImportDoctor(Imp)
# 创建请求webservice的客户端
client = Client('http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl',
                doctor=doctor)
# 使用客户端调服务器的接口
res = client.service.__getattr__('getWeatherbyCityName')('长沙')
print(res)