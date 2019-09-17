# -*- coding: utf-8 -*- 
# by Appetizer v1.4.7
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import os
from datetime import datetime

serialno = r'af0814d' # device adb serial
apk = r'D:\BaiduNetdiskDownload\【瑞客论坛 www.ruike1.com】移动端自动化测试Appium  从入门到项目实战Python版\wangjiao.apk'
output = os.getcwd()

desired_caps = {}
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = serialno
desired_caps['unicodeKeyboard'] = True # 可输入中文
desired_caps['resetKeyboard'] = True # 每次测试重置输入法
desired_caps['app'] = os.path.abspath(apk)
desired_caps["noReset"] = True # 每次测试不重新安装APP
desired_caps["fullReset"] = False

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5.0)
driver.find_element_by_accessibility_id("王教授").click()
driver.find_element_by_xpath("//[@resource-id='com.wangjiao.prof.wang:id/pw_main_leader_tl']/android.widget.LinearLayout[@index='0']/androidx.appcompat.app.a$c[@index='2']/android.widget.LinearLayout[@index='0']").click()
driver.find_element_by_id("com.wangjiao.prof.wang:id/pw_draggable_library_image_cv").click()
driver.find_element_by_xpath("//[@resource-id='com.wangjiao.prof.wang:id/pw_library_handbook_content_fl']/androidx.recyclerview.widget.RecyclerView[@index='0']/android.widget.LinearLayout[@index='2']").click()
webviews = driver.contexts
driver.switch_to.context(webviews[1]) # 开始使用Selenium API

driver.find_element_by_xpath("//[@resource-id='app']/android.view.View[@index='0']/android.view.View[@index='0']/android.view.View[@index='1']").click()
driver.find_element_by_xpath("//[@resource-id='app']/android.view.View[@index='2']/android.view.View[@index='1']/android.view.View[@index='1']/android.view.View[@index='0']/android.widget.ListView[@index='0']/android.widget.ListView[@index='2']/android.view.View[@index='0']").click()
driver.find_element_by_xpath("//*[@text='http://www.cygwin.com/']").click()
