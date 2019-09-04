#!/usr/bin/env python
# -*- coding: utf-8 -*-

_author_='百度搜索：小强测试品牌'
# @官网    : http://www.xqtesting.com
# @博客	: http://www.xqtesting.com/blog.html
# @微信公众号	: 测试帮日记

import time
from appium import webdriver

desired_caps = {
    #使用哪种移动平台。IOS、Android
    'platformName': 'Android',
    #启动哪种设备，是真机还是模拟器，可有可无
    'deviceName': 'Android Emulator',  
    #OS的版本
    'platformVersion': '4.4.4',

    #被测试的App在电脑上的绝对路径，如果写了这个就可以不写下面的两个了
    #缺点：每次执行都会重新安装！
    #'app': 'os.path.abspath("d:\\python_workspace\\AppiumClassDemo\\小米商城.apk")',

    #建议用下面这种写法
    # apk包名
    'appPackage': 'com.xiaomi.shop',
    # apk的launcherActivity
    #注意，原生app的话要在activity前加个.
    'appActivity': 'com.xiaomi.shop.activity.MainTabActivity',

    #隐藏手机中的软键盘,让手机中可以输入中文
    'unicodeKeyboard': True,
    'resetKeyboard': True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.implicitly_wait(5)

#广告页的跳过
driver.find_element('id', 'com.xiaomi.shop:id/skip').click()

#业务很重要啊，如果你不做这个点击就没办法输入关键字搜索
driver.find_element(
    'id', "com.xiaomi.shop.plugin.homepage:id/fragment_search_swither").click()

driver.find_element(
    'id', "com.xiaomi.shop2.plugin.search:id/input").send_keys("空气净化器")

driver.find_element(
    'id', "com.xiaomi.shop2.plugin.search:id/search_fragment_search_btn").click()

time.sleep(5)
driver.quit()
