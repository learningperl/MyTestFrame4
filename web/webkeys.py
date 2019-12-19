# coding=utf-8
import os, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Web:
    """
    封装Web自动化的常用操作
    """

    def __init__(self):
        # 定义实例变量，存储浏览器，这个浏览器可以在整个
        # 类里面被调用
        self.driver = None
        self.txt = ''

    def openbrowser(self, br=None, dr=None):
        """
        打开浏览器
        :param br:指定打开浏览器的类型
            （gc:谷歌；ff:火狐；ie:ie浏览器；默认为gc）
        :param dr:指定driver文件的位置
            （默认为：../lib/chromedriver）
        :return:
        """
        if br is None or br == '':
            br = 'gc'

        if dr is None or dr == '':
            if br == 'gc':
                dr = './web/lib/chromedriver'

            if br == 'ie':
                dr = './web/lib/IEDriverServer'

            if br == 'ff':
                dr = './web/lib/geckodriver'

        if br == 'gc':
            # 谷歌浏览器配置对象
            opt = Options()
            opt.add_argument('--user-data-dir=%s\\AppData\\Local\\Google'
                             '\\Chrome\\user data' % os.environ["USERPROFILE"])

            # 打开浏览器
            self.driver = webdriver.Chrome(options=opt,
                                           executable_path=dr)
            # 隐式等待
            self.driver.implicitly_wait(10)
        if br == 'ff':
            # opt = Options()
            # opt.add_argument('-profile=%s\\AppData\\Roaming\\Mozilla\Firefox\\Profiles\\rvuazmas.default' % os.environ["USERPROFILE"])

            # webdriver.Firefox.profile = r"C:\\Users\Will\AppData\Roaming\Mozilla\Firefox\Profiles\rvuazmas.default"
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.dir", "D:\\profile1")
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                   "application/octet-stream, application/vnd.ms-excel, text/csv, application/zip")
            profile.update_preferences()
            self.driver = webdriver.Firefox(executable_path=dr, firefox_profile=profile)

        if br == 'ie':
            self.driver = webdriver.Ie(executable_path=dr)

    def geturl(self, url):
        """
        打开网页地址
        :param url: 网站地址，必须以http/https开头
        :return: 无
        """
        self.driver.get(url)

    def click(self, xpath):
        """
        点击元素
        :param xpath: 定位元素的xpath
        :return: 无
        """
        ele = self.__findele(xpath)
        ele.click()

    def click_link(self, xpath):
        """
        点击a标签，针对selenium点击不了的情况
        （实现跳转的a标签，带href属性）
        :param xpath: 定位元素的xpath
        :return: 无
        """
        ele = self.__findele(xpath)
        href = ele.get_attribute('href')
        self.driver.get(href)

    def js_click(self, xpath):
        """
        点击a标签，针对selenium点击不了的情况
        （点击a标签触发js事件的，JavaScript:void(0);）
        :param xpath: 定位元素的xpath
        :return: 无
        """
        ele = self.__findele(xpath)
        self.driver.execute_script("$(arguments[0]).click()", ele)

    def input(self, xpath, value):
        """
        输入文本
        :param xpath: 定位元素的xpath
        :param value: 需要输入的文本
        :return: 无
        """
        ele = self.__findele(xpath)
        ele.send_keys(value)

    def gettext(self, xpath):
        """
        获取元素的文本
        :param xpath: 定位元素的xpath
        :return: 元素的文本
        """
        ele = self.__findele(xpath)
        self.txt = ele.text
        return self.txt

    def __findele(self, xpath):
        """
        封装xpath找元素的方法
        :param xpath: 定位元素的xpath
        :return: 找到的元素，如果没找到，就返回None
        """
        ele = self.driver.find_element_by_xpath(xpath)
        return ele

    def sleep(self, t=1):
        if t is None or t == '':
            t = 1
        else:
            t = int(t)

        time.sleep(t)

    def assertequals(self, exp_value, msg=''):
        """
        校验上一步获取的文本和期望值一样
        :param exp_value: 期望值
        :return: 是否一样
        """
        if self.txt == exp_value:
            print(msg + '校验成功')
            return True
        else:
            print(msg + '校验失败')
            return False

    def quit(self):
        """
        退出当前打开的浏览器
        :return: 无
        """
        self.driver.quit()
