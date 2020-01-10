# coding=utf-8
from appium import webdriver
import time


class QQauto:

    def __init__(self):
        """
        启动appium服务
        """
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0.1"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.mobileqq"
        caps["appActivity"] = ".activity.SplashActivity"
        caps["noReset"] = "true"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def login(self):
        """
        登录模块用例，
        由老Will负责
        :return:
        """
        el1 = self.driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
        el1.send_keys("3599292078")
        el3 = self.driver.find_element_by_accessibility_id("密码 安全")
        el3.click()
        el3.clear()
        el3.send_keys("xiaobao168")
        el4 = self.driver.find_element_by_accessibility_id("登录")
        el4.click()


    def logout(self):
        """
        退出登录
        老will负责
        :return:
        """
        time.sleep(20)
        try:
            el1 = self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabWidget/android.widget.RelativeLayout/android.view.View")
            el1.click()
        except Exception as e:
            print('没定位到')
        el5 = self.driver.find_element_by_accessibility_id("帐户及设置")
        el5.click()
        el6 = self.driver.find_element_by_accessibility_id("设置")
        el6.click()
        el7 = self.driver.find_element_by_id("com.tencent.mobileqq:id/account_switch")
        el7.click()
        el8 = self.driver.find_element_by_accessibility_id("退出当前帐号按钮")
        el8.click()
        el9 = self.driver.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn")
        el9.click()

    def quit(self):
        self.driver.quit()
