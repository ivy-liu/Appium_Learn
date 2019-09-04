import os,sys,time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from appium import webdriver
from forSwipe import ForSwipe
import selenium

capabilities={
  "platformName": "Android",
  "deviceName": "127.0.0.1:62001",
  "app": "D:\\python_code\Appium_Learn\\testing_software\\wangjiao.apk",
  # appPackage、appActivity,写了电脑上的绝对路径，这俩就不需要配置
  # 特点：1.这里不支持相对路径 2.每一次都重新安装

  # #这种写法比较好
  # #aapt dump badging apk的路径
  # #package: name='cn.com.open.mooc'
  # 'appPackage':'com.wangjiao.prof.wang',
  # #launchable-activity: name='cn.com.open.mooc.index.splash.MCSplashActivity'
  # #原生app要在activity前加个 .
  # 'appActivity':'prof.wang.activity.LaunchActivity',



  #隐藏手机中的软键盘，使手机中可以输入中文
  'unicodeKeyboard':True,
  'resetKeyboard':True
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',capabilities)
time.sleep(5)#不等待就有问题，隐性等待不行，有毒
# driver.implicitly_wait(5)
#滑动
sw=ForSwipe()
sw.swipeLeft(driver)
# driver.swipe(500,400,50,400,2000)    
# driver.implicitly_wait(5)
time.sleep(5)#不等待就有问题，隐性等待不行，有毒
sw.swipeLeft(driver)


# 轮播页后点击立即开启

#se 中的 id 对应 Appium中的 resource-id
driver.find_element('id','com.wangjiao.prof.wang:id/guide_start_tv').click()

# se 中的 class name 对应 Appium中的 class
elements=driver.find_elements('class name','android.widget.EditText')
elements[0].send_keys('17621152203')
elements[1].send_keys('qwe123123')

time.sleep(5)

# se 中的 name 对应Appium中的 text
# driver.find_element("name","登录").click()
driver.find_element_by_xpath('//button[contains(@*, "登录")]').click()


time.sleep(5)
driver.quit()