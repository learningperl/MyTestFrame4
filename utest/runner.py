import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('./', pattern='Pramatest.py')
    result = BeautifulReport(test_suite)
    result.report(filename='电商项目测试报告', description='电商项目测试报告')