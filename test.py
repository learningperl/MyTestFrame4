# # coding=utf-8
# import requests,jsonpath,json
#
#
# session = requests.session()
# session.headers['referer'] = 'https://ke.qq.com/course/317690'
# res = session.get('https://ke.qq.com/cgi-bin/comment_new/course_comment_list?cid=317690&count=10&page=0&filter_rating=0&bkn=&r=0.19680992383870177')
# jsonres = json.loads(res.text)
# value = jsonpath.jsonpath(jsonres,'$.result.items[0].nick_name')
# print(value[0])
# from common.Encrypt import *
#
# s = '[1111]'
#
#
# def use_encrypt(s):
#     """
#     替换加密后的字符串
#     :param s: 需要加密的字符串
#     :return: 加密后的字符串
#     """
#     # 递归的思维，当字符串里面既有[,又有]的时候
#     # 反复的执行如下替换
#     if s is None:
#         return ''
#     elif s.find('[') >= 0 and s.find(']') >= 0:
#         en_s = s[s.find('[') + 1:s.find(']')]
#         en_s1 = encrypt(en_s)
#         s = s.replace('[' + en_s + ']', en_s1)
#         return use_encrypt(s)
#     else:
#         return s
#
#
# s = use_encrypt(s)
# print(s)

s = 'abcdefghijklmnkldsajfas'
print(s[10:0])