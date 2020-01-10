# -*- coding: UTF-8 -*-
import unittest
from utest import testlib
from parameterized import parameterized


# 创建一个测试类，继承unittest
class PramaTest(unittest.TestCase):
    """
    参数化：单元测试参数化的参数使用的二维列表
    """

    @parameterized.expand([
        ['整数相加', 1, 1, 2],
        ['小数相加', 1.1, 1.33333333, 2.43333333],
        ['整数加字符串', 1, '1', '11'],
        ['整数加小数', 1, 1.1, 2.1],
    ])
    def test_add(self, name, x, y, z):
        """"""
        print(name)
        self.assertEqual(testlib.add(x, y), z)


if __name__ == '__main__':
    unittest.main()
