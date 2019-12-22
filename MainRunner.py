# coding=utf-8
from common.Excel import Reader,Writer
from inter.interkeys import HTTP
import inspect


print('我的数据驱动测试框架')


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



# 逐行读取excel
reader = Reader()
reader.open_excel('./lib/HTTP接口用例.xls')
writer = Writer()
writer.copy_open('./lib/HTTP接口用例.xls', './lib/result-HTTP接口用例.xls')

sheetname = reader.get_sheets()
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
            print(line)
            runcase(line,obj)


writer.save_close()