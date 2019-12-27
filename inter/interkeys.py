# coding=utf-8
import requests, json, jsonpath
from common import logger
from common.Encrypt import *


class HTTP:

    def __init__(self,writer):
        # session管理
        self.session = requests.session()
        # 基础的host地址
        self.url = ''
        # 结果解析
        self.result = None
        self.jsonres = None
        # 关联保存参数的字典
        self.relations = {}

        # 写入excel文件的Excel.Writer对象
        self.writer = writer
        # 记录当前需要写入的列
        self.row = 0

    def seturl(self, url):
        """
        设置基本url地址
        :param url:
        :return:
        """
        self.url = url
        self.__write_excel_res('PASS','设置成功：' + self.url)

    def get(self, path, params):
        """
        发送get请求
        :param path: 请求的路径
        :param params: 请求的参数
        :return: 无
        """
        params = self.__get_relations(params)
        self.result = self.session.get(self.url + '/' + path + '?' + params)
        try:
            self.jsonres = json.loads(self.result.text)
        except Exception as e:
            self.jsonres = None

        self.__write_excel_res('PASS',self.result.text)


    def post(self, path, params):
        """
        发送post请求
        :param path: 请求的路径
        :param params: 请求的参数
        :return: 无
        """
        params = self.__get_relations(params)
        params = self.__use_encrypt(params)
        self.result = self.session.post(self.url + '/' + path,
                                        data=self.__get_data(params))
        try:
            self.jsonres = json.loads(self.result.text)
        except Exception as e:
            self.jsonres = None

        self.__write_excel_res('PASS',self.result.text)

    def addheader(self, key, value):
        """
        在session上面添加头
        :param key: 头的键
        :param value: 头的值
        :return: 无
        """
        value = self.__get_relations(value)
        self.session.headers[key] = value
        self.__write_excel_res('PASS','添加成功：'+str(self.session.headers))

    def removeheader(self,key):
        """
        删除头里面的某一个键值对
        :param key: 要删除的键
        :return: 无
        """
        try:
            self.session.headers.pop(key)
        except Exception as e:
            pass
        self.__write_excel_res('PASS', '删除成功：' + str(self.session.headers))

    def __get_data(self,params):
        """
        将标准的url格式参数转换为字典
        :param params: url参数字符串
        :return: 转换后的字典
        """
        if params is None or params == '':
            # 如果是空或者空字符串，都返回None
            return None
        else:
            params_dict = {}
            # 分割url字符串的键值对
            list_params = params.split('&')
            # 遍历键值对
            for items in list_params:
                # 如果键值对里面有'='，那么我们就取=左边为键，=右边为值
                # 主要是支持值里面传'='
                if items.find('=') >= 0:
                    params_dict[items[0:items.find('=')]] = items[items.find('=') + 1:]
                else:
                    # 如果没有=，处理为键，值为空
                    params_dict[items] = None

            return params_dict

    def savejson(self,key,param_name):
        """
        保存关联的参数
        :param key: 需要保存的json结果里面的键
        :param param_name: 保存后参数的名字
        :return: 无
        """
        try:
            self.relations[param_name] = self.jsonres[key]
            self.__write_excel_res('PASS', self.relations)
        except Exception as e:
            self.relations[param_name] = ''
            self.__write_excel_res('FAIL', self.relations)

    def __get_relations(self,params):
        """
        将参数里面用到关联的地方，替换为关联后的值
        :param params: 关联前的参数
        :return: 关联后的结果
        """
        if params is None or params == '':
            return ''
        else:
            # 遍历当前保存后的参数字典
            # 然后把参数里面凡是符合：{keys}这种
            # 形式的字符串，都替换为relations这个字典里面keys这个键的值
            for keys in self.relations:
                params = params.replace('{' + keys + '}'
                                        ,self.relations[keys])

        return params

    def assertequals(self,jsonpathkey,value):
        """
        判断json结果里面某个键的值是否和期望值value相等
        :param key: json的键
        :param value: 期望值
        :return: 是否相等
        """
        res = None
        try:
            res = str(jsonpath.jsonpath(self.jsonres,jsonpathkey)[0])
        except Exception as e:
            pass
        # 关联
        value = self.__get_relations(value)
        if str(res) == str(value):
            logger.info('PASS')
            self.__write_excel_res('PASS', res)
            return True
        else:
            logger.info('FAIL')
            self.__write_excel_res('FAIL', res)
            return False

    def __write_excel_res(self,status,msg):
        # 写入excel
        self.writer.write(self.row,7,status)
        self.writer.write(self.row,8,str(msg))

    def __use_encrypt(self,params):
        """
        替换加密后的字符串
        :param s: 需要加密的字符串
        :return: 加密后的字符串
        """
        # 递归的思维，当字符串里面既有[,又有]的时候
        # 反复的执行如下替换
        if params is None:
            return ''
        elif params.find('[') >= 0 and params.find(']') >= 0:
            en_s = params[params.find('[') + 1:params.find(']')]
            en_s1 = encrypt(en_s)
            params = params.replace('[' + en_s + ']', en_s1)
            return self.__use_encrypt(params)
        else:
            return params