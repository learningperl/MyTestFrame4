# -*- coding: UTF-8 -*-
import unittest
from utest import datadriven
from parameterized import parameterized
from inter.interkeys import HTTP


# 创建一个测试类，继承unittest
class DataRunner(unittest.TestCase):
    """
    参数化：单元测试参数化的参数使用的二维列表
    """

    obj = None

    @classmethod
    def setUpClass(cls) -> None:
        if datadriven.runtype == 'HTTP':
            cls.obj = HTTP(datadriven.writer)

    @parameterized.expand(datadriven.alllist)
    def test_(self, index, name, keyword, param1, param2, param3):
        """"""
        print(name)
        line = [keyword, param1, param2, param3]

        try:
            index = int(index)
            self.obj.row = index
            # 反射获取函数
            func = datadriven.geffunc(line, self.obj)
            # 获取函数参数个数
            lenargs = datadriven.getargs(func)
            # 执行关键字
            res = datadriven.run(func, lenargs, line)
            self.assertTrue(res)
        except:
            datadriven.writer.set_sheet(index)


