import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from appium import webdriver
capabilities={
  "platformName": "Android",
  "deviceName": "127.0.0.1:62001",
  "app": "D:\python_code\Appium_Learn\testing_software\mukewang.apk"
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',capabilities)
#滑动
driver.swipe(500,400,50,400)
driver.swipe(500,400,50,400,2000)