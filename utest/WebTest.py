# coding=utf-8
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Web(unittest.TestCase):
    """
    继承unittest的测试类，
    Web这个类就是unittest的一个单元测试类
    """

    driver = None

    # def setUp(self) -> None:
    #     """
    #     每一个测试函数运行之前都会执行
    #     :return:
    #     """
    #     print('开始测试')
    #
    # def tearDown(self) -> None:
    #     """
    #     每一个测试函数运行之后都会执行
    #     :return:
    #     """
    #     print('测试结束')

    @classmethod
    def setUpClass(cls) -> None:
        """
        整个测试开始前执行
        :return:
        """
        print('测试开始\n')
        # 谷歌浏览器配置对象
        opt = Options()
        opt.add_argument('--user-data-dir=%s\\AppData\\Local\\Google'
                         '\\Chrome\\user data' % os.environ["USERPROFILE"])

        # 打开浏览器
        cls.driver = webdriver.Chrome(options=opt,
                                      executable_path='../web/lib/chromedriver')
        # 隐式等待
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        """
        整个测试结束后执行
        :return:
        """
        cls.driver.quit()
        print('测试结束')

    def test_1_login(self):
        print('登录页面')
        self.driver.get('http://testingedu.com.cn:8000/Home/user/login.html')
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('13800138006')
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@id="verify_code"]').send_keys('1111')
        self.driver.find_element_by_xpath('//*[@id="loginform"]/div/div[6]/a').click()
        time.sleep(2)
        text = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/a[1]').text
        self.assertEqual(text, 'summer')

    def test_2_switch(self):
        print('窗口切换')
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[1]/a').click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        title = self.driver.title
        self.assertEqual(title, '我的订单')
