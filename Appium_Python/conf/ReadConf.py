# -*- coding: UTF-8 -*-

__author__ = 'rain'

from configparser import ConfigParser
import os
from os import path

prjDir = os.path.split(os.path.realpath(__file__))[0]
conf_path = os.path.join(prjDir, "conf.ini")
# rootdir = os.getcwd()
# absdir = os.path.abspath('confi.ini')
# realdir = os.path.realpath(__file__)
d = path.dirname(__file__)
parentdir = os.path.dirname(d)


# 加载配置文件路径
def load_config(file_path):
    # 实例化ConfigParser对象
    cfg = ConfigParser()
    try:
        if os.path.exists(file_path):
            # 读取文件路径
            cfg.read(file_path)
            # print()
            return cfg
    except:
        print("%s is not exit" %file_path)

# 获取配置文件设置
def get_config(section, option):
    cf = load_config(conf_path)
    return cf.get(section, option)

# 打印配置文件中section
def print_sections():
    cf = load_config(conf_path)
    return cf.sections()

# 打印配置文件中的options
def print_opthons(section):
    cf = load_config(conf_path)
    return cf.options(section)

# 读取AndroidInfo配置
def read_appInfo():
    cf = load_config(conf_path)
    # 将读取的配置信息存放在字典中
    app_dict = {}

    section = 'AndroidInfo'
    app_dict['platformName'] = cf.get(section, 'platformName')
    app_dict['platformVersion'] = cf.get(section, 'platformVersion')
    app_dict['deviceName'] = cf.get(section, 'deviceName')
    app_dict['appPackage'] = cf.get(section, 'appPackage')
    app_dict['appActivity'] = cf.get(section, 'appActivity')

    # 开启键盘输入，支持中文
    app_dict['unicodeKeyboard'] = cf.get(section, 'unicodeKeyboard')
    app_dict['resetKeyboard'] = cf.get(section, 'resetKeyboard')

    app_dict['newCommandTimeout'] = cf.get(section, 'newCommandTimeout')
    app_dict['noReset'] = cf.get(section, 'noReset')

    print("%s 启动APP配置信息：%s" %(section, app_dict))
    return app_dict

if __name__ == '__main__':

    load_config(conf_path)
    print(prjDir)
    print(conf_path)
    # read_appInfo()
    # print(rootdir)
    # print(absdir)
    # print(realdir)
    print(parentdir)
