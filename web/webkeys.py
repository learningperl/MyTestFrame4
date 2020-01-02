# coding=utf-8
import os, time, traceback
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

from common import logger



class Web:
    """
    封装Web自动化的常用操作
    """

    def __init__(self,writer):
        # 定义实例变量，存储浏览器，这个浏览器可以在整个
        # 类里面被调用
        self.driver = None
        self.txt = ''
        # 写入结果
        self.row = 0
        self.writer = writer
        # 关联的参数
        self.params = {}

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

        try:
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

            self.__write_excel_res('PASS','打开浏览器成功')
        except Exception as e:
            self.__write_excel_res('FAIL',traceback.format_exc())
            logger.exception(e)
            # 程序在这个异常时，停止运行
            self.writer.save_close()
            exit(-1)

    def geturl(self, url):
        """
        打开网页地址
        :param url: 网站地址，必须以http/https开头
        :return: 无
        """
        try:
            self.driver.get(url)
            self.__write_excel_res('PASS', '打开url成功')
        except Exception as e:
            self.__write_excel_res('FAIL',traceback.format_exc())
            logger.exception(e)

    def click(self, xpath):
        """
        点击元素
        :param xpath: 定位元素的xpath
        :return: 无
        """
        try:
            ele = self.__findele(xpath)
            ele.click()
            self.__write_excel_res('PASS', '点击元素成功')
        except Exception as e:
            self.__write_excel_res('FAIL', traceback.format_exc())
            logger.exception(e)

    def click_link(self, xpath):
        """
        点击a标签，针对selenium点击不了的情况
        （实现跳转的a标签，带href属性）
        :param xpath: 定位元素的xpath
        :return: 无
        """
        try:
            ele = self.__findele(xpath)
            href = ele.get_attribute('href')
            self.driver.get(href)
            self.__write_excel_res('PASS', '点击元素成功')
        except Exception as e:
            self.__write_excel_res('FAIL', traceback.format_exc())
            logger.exception(e)

    def js_click(self, xpath):
        """
        点击a标签，针对selenium点击不了的情况
        （点击a标签触发js事件的，JavaScript:void(0);）
        :param xpath: 定位元素的xpath
        :return: 无
        """
        try:
            ele = self.__findele(xpath)
            self.driver.execute_script("$(arguments[0]).click()", ele)
            self.__write_excel_res('PASS', '点击元素成功')
        except Exception as e:
            self.__write_excel_res('FAIL', traceback.format_exc())
            logger.exception(e)

    def input(self, xpath, value):
        """
        输入文本
        :param xpath: 定位元素的xpath
        :param value: 需要输入的文本
        :return: 无
        """
        try:
            ele = self.__findele(xpath)
            ele.send_keys(value)
            self.__write_excel_res('PASS', '元素输入文本成功')
        except Exception as e:
            self.__write_excel_res('FAIL', traceback.format_exc())
            logger.exception(e)

    def gettitle(self,paramname):
        """
        获取元素的文本
        :param xpath: 定位元素的xpath
        :return: 元素的文本
        """
        try:
            self.params[paramname] = self.driver.title
            self.__write_excel_res('PASS', '获取元素文本成功：' + self.txt)
            return self.txt
        except Exception as e:
            self.params[paramname] = ''
            self.__write_excel_res('FAIL', traceback.format_exc())
            logger.exception(e)
            return None

    def gettext(self, xpath,paramname):
        """
        获取元素的文本
        :param xpath: 定位元素的xpath
        :return: 元素的文本
        """
        try:
            ele = self.__findele(xpath)
            self.params[paramname] = ele.text
            self.__write_excel_res('PASS', '获取元素文本成功：' + self.params[paramname])
            return self.params[paramname]
        except Exception as e:
            self.params[paramname] = ''
            self.__write_excel_res('FAIL', traceback.format_exc())
            logger.exception(e)
            return None


    def switchwindow(self,idx):
        try:
            # 窗口下标的列表
            handles = self.driver.window_handles
            # print(handles)
            # 切换到指定下标的窗口
            self.driver.switch_to.window(handles[int(idx)])
            self.__write_excel_res('PASS', '窗口切换成功')
        except Exception as e:
            self.__write_excel_res('FAIL', traceback.format_exc())
            logger.exception(e)

    def switchiframe(self,xpath):
        try:
            # 获取iframe
            ele = self.__findele(xpath)
            # print(handles)
            # 切换到指定下标的窗口
            self.driver.switch_to.frame(ele)
            self.__write_excel_res('PASS', 'frame切换成功')
        except Exception as e:
            self.__write_excel_res('FAIL', traceback.format_exc())
            logger.exception(e)

    def switchout(self):
        try:
            # 切换HTML页面
            self.driver.switch_to.default_content()
            self.__write_excel_res('PASS', 'frame切换成功')
        except Exception as e:
            self.__write_excel_res('FAIL', traceback.format_exc())
            logger.exception(e)

    def moveto(self,xpath):
        try:
            ele = self.__findele(xpath)
            # 把鼠标移动到元素
            actions = ActionChains(self.driver)
            actions.move_to_element(ele).perform()
        except Exception as e:
            self.__write_excel_res('FAIL', traceback.format_exc())
            logger.exception(e)

    def excutejs(self,js):
        try:
            time.sleep(2)
            self.driver.execute_script(js)
        except Exception as e:
            self.__write_excel_res('FAIL', traceback.format_exc())
            logger.exception(e)

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
        self.__write_excel_res('PASS', '')

    def assertequals(self,paramname , exp_value, msg=''):
        """
        校验上一步获取的文本和期望值一样
        :param exp_value: 期望值
        :return: 是否一样
        """
        paramname = self.__get_relations(paramname)
        if (not paramname is None) and paramname == exp_value:
            print(msg + '校验成功')
            self.__write_excel_res('PASS', paramname)
            return True
        else:
            print(msg + '校验失败')
            self.__write_excel_res('FAIL', paramname)
            return False

    def quit(self):
        """
        退出当前打开的浏览器
        :return: 无
        """
        try:
            self.driver.quit()
            self.__write_excel_res('PASS', '')
        except Exception as e:
            self.__write_excel_res('FAIL', traceback.format_exc())
            logger.exception(e)


    def __write_excel_res(self,status,msg):
        # 写入excel
        self.writer.write(self.row,7,status)
        self.writer.write(self.row,8,str(msg))

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
            for keys in self.params:
                params = params.replace('{' + keys + '}'
                                        ,self.params[keys])

        return params