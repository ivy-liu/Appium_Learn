import time
from appium import webdriver
from forSwipe import ForSwipe


def get_driver():
    capabilities = {
        "platformName": "Android",
        "deviceName": "192.168.75.103:5555",
        "app": "D:\\python_code\\Appium_Learn\\testing_software\\wangjiao.apk",
        # appPackage、appActivity,新版本不需要写，如果appium报错出现activity期待与实际不符，
        # 尝试appWaitActivity,配置appium报错中Found package中的activity

        # 邮箱，不许再次安装直接打开到登录页
        "noReset": "true",


        # 隐藏手机中的软键盘，使手机中可以输入中文
        'unicodeKeyboard': True,
        'resetKeyboard': True

    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
    return driver


driver = get_driver()


def go_login():
    # 使用id
    # 轮播图后点击确认开启，相册权限获取
    driver.find_element_by_id(
        "com.wangjiao.prof.wang:id/guide_start_tv").click()
    driver.find_element_by_id(
        'com.android.packageinstaller:id/permission_allow_button').click()


def password_login():
    # 录入密码登录账号
    time.sleep(1)
    driver.find_element_by_id(
        'com.wangjiao.prof.wang:id/pw_login_pwd_mobile_et').send_keys('17621152203')
    driver.find_element_by_id(
        'com.wangjiao.prof.wang:id/pw_login_pwd_pwd_et').send_keys('qwe123123')
    driver.find_element_by_id(
        'com.wangjiao.prof.wang:id/pw_login_login_btn').click()


def change_tab():
    # 使用层级
    # 切换tab
    time.sleep(1)
    # 如果直接点击，会默认点第一个
    elements = driver.find_elements_by_class_name('androidx.appcompat.app.a$c')
    elements[2].click()


def search_data():
    # 使用Uiautomator
    # 录入搜索框-还没学会用键盘
    time.sleep(1)
    driver.find_element_by_id(
        'com.wangjiao.prof.wang:id/pw_include_search_click_bar_search_ll').click()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.wangjiao.prof.wang:id/pw_library_search_ce")').send_keys('负载')
    # driver.find_element_by_xpath('//*[contains(@text,"您好，请问有什么可以帮您？")]').send_keys('hahah')#可以录入成功
    # 隐藏手机中的软键盘，使手机中可以输入中文
    # 'unicodeKeyboard':True,
    # 'resetKeyboard':True

    # 点击取消
    driver.find_element_by_android_uiautomator(
        'new UiSelector().text("取消")').click()


def to_log_out():
    # 使用xpath
    # 退出登录
    time.sleep(1)
    # 我的
    driver.find_element_by_xpath('//*[contains(@text,"我的")]').click()
    time.sleep(1)
    # 设置
    driver.find_element_by_xpath(
        '//android.widget.TextView[contains(@text,"设置")]').click()
    time.sleep(1)
    # 退出登录
    driver.find_element_by_xpath(
        '//android.widget.Button[@text="退出登录"]').click()
    time.sleep(1)
    # 确认 取取消，取取消的父节点，取取消的父节点的子节点
    driver.find_element_by_xpath(
        '//android.widget.TextView[@text="取消"]/../androidx.recyclerview.widget.RecyclerView').click()

def zhiku():
  #webview
  #智库-列表-点击查看

  time.sleep(1)
  #切换至智库
  driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.wangjiao.prof.wang:id/pw_main_tab_item_view_title_icon"and@text="智库"]').click()
  # print('r--',r)
  time.sleep(1)
  #点击打开书册《数据库》
  driver.find_element_by_id('com.wangjiao.prof.wang:id/pw_draggable_library_image_iv').click()
  #打开文章Cygwin
  driver.find_element_by_xpath('//*[contains(@text,"Cygwin")]').click()
  

# sw = ForSwipe(driver)
# time.sleep(5)
# sw.swipe_on('left')
# time.sleep(1)
# sw.swipe_on('left')
# time.sleep(1)
# go_login()
# password_login()
# change_tab()
# search_data()
# to_log_out()
zhiku()