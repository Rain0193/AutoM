# -*- coding: UTF-8 -*-

__author__ = 'rain'
'''
参考文档：https://anikikun.gitbooks.io/appium-girls-tutorial/content/Up_uiautomator.html
'''

from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

global driver
# 设置配置信息
desired_caps = {}
desired_caps['device']='android'
desired_caps['platformName']='Android'
desired_caps['version']='4.4'
desired_caps['deviceName']='GWY7N17704003267'
# 获取PackageName, launchActivity （Android SDK tool中aapt dump badging xxx.apk）
desired_caps['appPackage']='cn.thecover.www.covermedia'
desired_caps['appActivity']='.ui.activity.FlashActivity'

# 启动回话连接appium server
driver = webdriver.Remote('http://127.0.0.1/wd/hub', desired_caps)

time.sleep(1)

'''
元素定位
    1.id定位->resouceid  # id是唯一的，多个相同resourceid可以通过index
    2.classname定位      # classname不一定唯一
    3.xpath定位          # xpath定位效率慢
    4.name定位           # appium1.6版本已去掉 
    4.name定位           # appium1.6版本已去掉 
'''

# id 定位控件
driver.find_element_by_id(" ")          # 控件唯一
driver.find_element_by_id(" ")[index]   # 多个相同resourceid可以通过index

# text 定位控件
driver.find_element_by_name("text")     # 已弃用
driver.find_element_by_xpath("//*[@text= '%s']" % (text))  # 可替代 find_element_by_name

# Accessibility ID在Android上面就等同于contentDescription
driver.find_element_by_accessibility_id("contentDescription")

# 层级定位 通过父节点找到子节点 list列表里面
ele = driver.find_element_by_id("parent_id")
eles = driver.find_element_by_id("child_id")[index]

# touchaction可以用来实现点击坐标，滑动等操作
# 点击操作
TouchAction(driver).press(None, x, y).release().perform()
# 滑动操作
TouchAction(driver).press(None, x, y).wait(20).move_to(None, dx, dy).release().perform()
# 长按控件
action = TouchAction(driver).long_press(el, 20000).perform()
time.sleep(20)
action.release().perform()

# Scroll 对于listview 滑动控件
driver.scroll(ele1, ele2)
# 物理按键keyenvent
driver.keyevent(3)          # Home键
# 隐藏键盘
driver.hide_keyboard()

# UI Automator 定位
driver.find_element_by_android_uiautomator('new Uiselector().text("text")')

# text 模糊定位
driver.find_element_by_android_uiautomator('new Uiselector().textContains("text")')

# text 正则匹配
driver.find_element_by_android_uiautomator('new Uiselector().texMathces("^text.*")')

# resourceID
driver.find_element_by_android_uiautomator('new Uiselector().resourceId("resourceID")')

driver.find_element_by_android_uiautomator('new Uiselector().resourceIdMatches(".+text")')

# className
driver.find_element_by_android_uiautomator('new Uiselector().className("className")')
driver.find_element_by_android_uiautomator('new Uiselector().classNameMatchs(".*Editext")')
# 滑动查找listview包含text的控件
driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains(\"上课中\"))")




# 封装曲线滑动 滑动速度不能太快
def swipe(points):
    last_x = 0
    last_y = 0
    swipe_action = TouchAction(driver)
    for i in range(0, len(points)):
        x = points[i][0]
        y = points[i][1]
        if i == 0:
            swipe_action = swipe_action .press(None, x, y).wait(20)
        elif i == (len(points) - 1):
            swipe_action = swipe_action.move_to(None, x - last_x, y - last_y).release()
            swipe_action.perform()
        else:
            swipe_action = swipe_action.move_to(None, x - last_x, y - last_y).wait(20)
        last_x = x
        last_y = y

# 封装多方式定位控件函数
def fin_for_element(xpath=None, id=None, text=None, index=None, timeout=3):
    start_time = time.time()
    now_time = time.time()
    while now_time - start_time < timeout:
        try:
            if xpath is not None:
                el = driver.find_element_by_xpath(xpath)
                return el
        except:
            pass
        try:
            if id is not None:
                if index is not None:
                    return driver.find_element_by_id(id)[index]
                else:
                    return driver.find_element_by_id(id)
        except:
            pass
        try:
            if text is not None:
                return driver.find_element_by_name(text)
        except:
            pass

        now_time = time.time()











# 退出会话
driver.quit()