# -*- coding: UTF-8 -*-

__author__ = 'rain'

from appium import  webdriver         # 安装appium python client
from conf import ReadConf
import requests
import time


# 读取启动APP配置信息
desired_caps = ReadConf.read_appInfo()

ip = ReadConf.get_config('AndroidInfo', 'ip')
port = ReadConf.get_config('AndroidInfo', 'port')
# 拼接appium server URL 地址
server_url = 'http://' + ip + ':' + port + '/wd/hub'

# 启动appium连接，先启动appium桌面版客户端
def start_driver():
    print("Start Driver...连接中...")
    retry = 0
    while retry < 2:                                                    # 连接失败重试一次
        try:
            driver = webdriver.Remote(server_url, desired_caps)         # 初始化driver
            time.sleep(10)                                              # 设置等待时间等待连接
            return driver
        except Exception as e:
            retry += 1
            if retry == 2:
                raise e

# 检查appium sever 是否连接正常
def is_running():
    url = server_url + '/status'
    # 请求url返回200 连接正常
    response = requests.get(url)
    print("response...%s" %response)
    if str(response.status_code).startswith('2'):
        print("Driver is running...连接正常...")
        return True
    else:
        return False

if __name__ == '__main__':
    start_driver()
    is_running()