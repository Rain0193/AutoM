# -*- coding: UTF-8 -*-

__author__ = 'rain'

import os
import sys
from configparser import ConfigParser

class ConfigIni():
    def __init__(self, confpath):
        self.current_directory = os.path.split(os.path.realpath(sys.argv[0]))[0]
        self.path = os.path.split(__file__)[0].replace('util', confpath)
        self.cf = ConfigParser()
        self.cf.read(self.path)

    # 获取配置文件section和option对应的值
    def get_ini(self, section, option):
        return self.cf.get(section, option)

    # 修改配置文件section和option对应的值
    def set_ini(self, section, option, value):
        self.cf.set(section, option, value)
        return self.cf.write(open(self.path, "wb"))
    # 添加配置文件section
    def add_ini(self, section):
        self.cf.add_section(section)
        return self.cf.write(open(self.path))

    def get_options(self, data):
        return self.cf.options(data)


if __name__ == '__main__':
    cfg = ConfigIni('conf/conf.ini')
    print(cfg.get_ini('AndroidInfo', 'appPackage'))
    cfg.add_ini('Test')