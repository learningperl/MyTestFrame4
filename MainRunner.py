# coding=utf-8
from common.Excel import Reader,Writer
from inter.interkeys import HTTP
import inspect
from common import logger
from common import config
from common.mysql import Mysql
import time
from common.excelresult import Res
from common.mail import Mail
from common.txt import Txt


logger.info('我的数据驱动测试框架')


def runcase(line,obj):
    """
    执行每一行用例
    :param line: 用例的数据列表
    :param obj: 执行用例的关键字对象
    :return: 无
    """
    # 反射获取到要执行的关键字
    func = getattr(obj, line[3])
    # 获取参数列表
    params = inspect.getfullargspec(func).__str__()
    params = params[params.find('args=') + 5:params.find(', varargs')]
    params = eval(params)
    params.remove('self')

    # 执行
    if len(params) == 0:
        func()
    elif len(params) == 1:
        func(line[4])
    elif len(params) == 2:
        func(line[4],line[5])
    elif len(params) == 3:
        func(line[4],line[5],line[6])
    else:
        print('暂时不支持超过3个参数的关键字')



# 读配置文件
config.get_config('./conf/conf.properties')
logger.info(config.config)

# 初始化数据库
mysql = Mysql()
mysql.init_mysql('./conf/userinfo.sql')

# 逐行读取excel
reader = Reader()
casename = 'HTTP接口用例-all'
reader.open_excel('./lib/%s.xls' % casename)
writer = Writer()
writer.copy_open('./lib/%s.xls' % casename, './lib/result-%s.xls' % casename)

sheetname = reader.get_sheets()
writer.set_sheet(sheetname[0])
starttime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
writer.write(1,3,starttime)
reader.readline()
casetype = reader.readline()[1]
# 执行用例的关键字库对象
obj = None
if casetype == 'HTTP':
    # 执行http接口自动化
    obj = HTTP(writer)

for sheet in sheetname:
    # 设置当前读取的sheet页面
    reader.set_sheet(sheet)
    # 读到哪个sheet页，写到哪个sheet页
    writer.set_sheet(sheet)
    for i in range(reader.rows):
        line = reader.readline()
        # 读到哪一行，写到哪一行
        obj.row = i
        if len(line[0]) >0 or len(line[1]) > 0:
            # 分组信息，不用执行
            pass
        else:
            # 执行用例
            logger.info(line)
            runcase(line,obj)

writer.set_sheet(sheetname[0])
endtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
writer.write(1,4,endtime)
writer.save_close()

# 结果统计
res = Res()
details = res.get_res('./lib/result-%s.xls' % casename)
r = res.get_groups('./lib/result-%s.xls' % casename)

# 邮件处理
mail = Mail()
htmlmodule = Txt('./conf/'+config.config['mailtxt'])
html = htmlmodule.read()[0]
# 对模块文本进行处理
# 替换总体统计信息
sumlist = ['status','passrate','starttime','endtime']
for s in sumlist:
    html = html.replace(s,details[s])

# 生成HTML的一行内容
alltrs = ''
for s in r:
    tr = '<tr><td width="100" height="28" align="center" bgcolor="#FFFFFF" style="border:1px solid #ccc;">分组信息</td><td width="80" height="28" align="center" bgcolor="#FFFFFF" style="border:1px solid #ccc;">用例总数</td><td width="80" align="center" bgcolor="#FFFFFF" style="border:1px solid #ccc;">通过数</td><td width="80" align="center" bgcolor="#FFFFFF" style="border:1px solid #ccc;">状态</td></tr>'
    tr = tr.replace('分组信息',str(s[0]))
    tr = tr.replace('用例总数', str(s[1]))
    tr = tr.replace('通过数', str(s[2]))
    tr = tr.replace('状态', str(s[3]))
    alltrs += tr

html = html.replace('mailbody',alltrs)

mail.send(html)
