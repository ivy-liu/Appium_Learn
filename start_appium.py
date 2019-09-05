import os,sys,time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from appium import webdriver
from forSwipe import ForSwipe
import selenium
from appium.webdriver.common.touch_action import TouchAction
# UiDevice，UiSelector，UiObject
# UiDevice此类主要包含了获取设备状态信息
# UiSelector主要是通过一定查询方式，定位到所要操作的UI元素
# UiObject可代表页面的任意元素，它的各种属性定位通常通过UiSelector来完成

capabilities={
  "platformName": "Android",
  "deviceName": "127.0.0.1:62001",
  # "app": "D:\\python_code\Appium_Learn\\testing_software\\wangjiao.apk",
  # # appPackage、appActivity,写了电脑上的绝对路径，这俩就不需要配置
  # # 特点：1.这里不支持相对路径 2.每一次都重新安装

  #这种写法比较好
  #aapt dump badging apk的路径
  #package: name='cn.com.open.mooc'
  'appPackage':'com.wangjiao.prof.wang',
  #launchable-activity: name='cn.com.open.mooc.index.splash.MCSplashActivity'
  #原生app要在activity前加个 .
  'appActivity':'prof.wang.activity.LaunchActivity',



  #隐藏手机中的软键盘，使手机中可以输入中文
  'unicodeKeyboard':True,
  'resetKeyboard':True
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',capabilities)
time.sleep(5)#不等待就有问题，隐性等待不行，有毒
# driver.implicitly_wait(5)

#滑动，初始安装打开广告页面
sw=ForSwipe()
sw.swipeLeft(driver)
# driver.swipe(500,400,50,400,2000)    
# driver.implicitly_wait(5)
time.sleep(5)#不等待就有问题，隐性等待不行，有毒
sw.swipeLeft(driver)


# 轮播页后点击立即开启
#se 中的 id 对应 Appium中的 resource-id
driver.find_element('id','com.wangjiao.prof.wang:id/guide_start_tv').click()

#权限获取，夜神5登录后出来这个，Genymotion先权限获取后登录
#照片、媒体内容获取，点击允许，这句安卓8可以，安卓其他不可以，是不是有毒
driver.find_element('id','com.android.packageinstaller:id/permission_allow_button').click()
time.sleep(5)


#登录
# # se 中的 class name 对应 Appium中的 class
elements=driver.find_elements('class name','android.widget.EditText')
print('eles--',elements)
elements[0].send_keys('17621152203')
elements[1].send_keys('qwe123123')

# driver.find_element('id','com.wangjiao.prof.wang:id/pw_login_pwd_mobile_et').send_keys('17621152203')
# driver.find_element('id','com.wangjiao.prof.wang:id/pw_login_pwd_pwd_et').send_keys('qwe123123')

time.sleep(5)

# se 中的 name 对应Appium中的 text ,不行，换一种
# driver.find_element("text","登录").click()

driver.find_element('id','com.wangjiao.prof.wang:id/pw_login_login_btn').click()
print('-完成登入-')
#以上Genymotion安卓6.0通，登录成功

# #切换至智库
# # 必须要Android4.0以上才能使用。因为只有4.0以上才带uiautomator工具。
# # 并且如果在定位时想要使用使用资源id来定位控件的话，则必须在API18以上。

time.sleep(5)
# driver.find_element('id','com.wangjiao.prof.wang:id/pw_main_tab_item_view_icon_iv').click()
driver.find_element_by_xpath('//*[@class name="android.widget.LinearLayout"]')
#点击搜索框
driver.find_element('id','com.wangjiao.prof.wang:id/pw_include_search_click_bar_search_ll').click()
#录入搜索内容
driver.find_element('id','com.wangjiao.prof.wang:id/pw_library_search_ce').send_keys('负载均衡')
time.sleep(3)


# # 登出
# #切换tab
# driver.implicitly_wait(5)
# time.sleep(3)
# driver.find_element_by_xpath('//*[@class="android.widget.LinearLayout"][4]').click()

# #点击设置
# driver.find_element('id','com.wangjiao.prof.wang:id/pw_custom_mine_item_cl').click()

# #点击登出
# driver.find_element('id','com.wangjiao.prof.wang:id/pw_setting_out_btn').click()
# #确定
# driver.find_element('id','com.wangjiao.prof.wang:id/pw_pop_menu_confirm_tv').click()
# print('-完成登出-')


time.sleep(5)
driver.quit()