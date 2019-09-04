'''
滑动封装
swipe(int start x,int start y,int end x,int y,duration)

int start x 开始滑动的x坐标
int start y 开始滑动的y坐标
int end x 结束滑动的x坐标
int end y 结束滑动的y坐标

犹豫分辨率每个手机各不相同，不能使用全部
应该获取手机的坐标来滑动
'''


class ForSwipe:

    # 获取机器品目的大小x,y
    def getSize(self, driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        # print('x,y-',x,y)
        return (x, y)

    # 屏幕向上滑动
    def swipeUp(self, driver, t=2000):
        size = self.getSize(driver)
        x1 = int(size[0]*0.5)  # x坐标
        y1 = int(size[1]*0.75)  # y初始坐标
        y2 = int(size[1]*0.25)  # y终点坐标
        driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向下滑动
    def swipeDown(self, driver, t=2000):
        size = self.getSize(driver)
        x1 = int(size[0]*0.5)  # x坐标
        y1 = int(size[1]*0.25)  # y初始坐标
        y2 = int(size[1]*0.75)  # y终点坐标
        driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动
    def swipeLeft(self, driver, t=2000):
        # print('执行了吗？')
        size = self.getSize(driver)
        x1 = int(size[0]*0.75)  # x坐标
        y1 = int(size[1]*0.5)  # y初始坐标
        x2 = int(size[0]*0.05)  # x终点坐标
        driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipeRight(self, driver, t=2000):
        size = self.getSize(driver)
        x1 = int(size[0]*0.05)  # x坐标
        y1 = int(size[1]*0.5)  # y初始坐标
        x2 = int(size[0]*0.75)  # x终点坐标
        driver.swipe(x1, y1, x2, y1, t)
