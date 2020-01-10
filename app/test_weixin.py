# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import os
import time

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "9"
caps["deviceName"] = "3e5d55a"
caps["appPackage"] = "com.tencent.mm"
caps["appActivity"] = ".ui.LauncherUI"
caps["noReset"] = "true"
caps["unicodeKeyboard"] = "true"
caps["resetKeyboard"] = "true"
caps["automationName"] = "UiAutomator1"

# 连接appium服务器
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(15)

el1 = driver.find_element_by_id("com.tencent.mm:id/r_")
el1.click()
el2 = driver.find_element_by_id("com.tencent.mm:id/m7")
el2.send_keys("京东购物")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.LinearLayout")
el3.click()

time.sleep(5)
os.popen('adb shell input tap 500 285')
time.sleep(2)

el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View")
el5.send_keys("手机")
time.sleep(2)
el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[3]/android.view.View[1]")
el6.click()
el7 = driver.find_element_by_id("goods-item-1-0-100010338198")
el7.click()
el8 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[17]/android.view.View[5]")
el8.click()

driver.quit()