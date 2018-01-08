# -*- coding: UTF-8 -*-
__author__ = 'rain'
'''

'''
from conf import ReadConf
import os
import time
import logging
import sys

def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

# 实现日志装饰器
def l():
    '''
    打印log，文件名+函数名
    :return:
    '''
    def log(func):
        def wrapper(*args, **kwargs):
            t = func(*args, **kwargs)
            filename = str(sys.argv[0].split('/')[-1].split('.')[0])
            Logging.success('{}:{}, return:{}'.format(filename, func.__name__, t))
            return t
        return wrapper
    return log

# 自定义log收集处理-
class Log():
    def __init__(self, element):
        self.el = element

    def mylogger(self, msg, flag=1):
        log_path = ReadConf.get_config('log', 'log_path')
        if not os.path.isdir(log_path):
            os.makedirs(log_path)

        log_name = 'fm_' + time.strftime('%Y%m%d%H%M%S') + '.log'
        file_log = log_path + log_name

        logging.basicConfig(filename=file_log,
                            level=logging.DEBUG,
                            filemode='w',
                            format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s:%(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S')
        if flag == 0:
            logging.debug(msg)
        elif flag == 1:
            logging.info(msg)
        elif flag == 2:
            logging.warning(msg)
        elif flag == -1:
            logging.error(msg)

# 自定义print打印输出信息带颜色
class colour:
    @staticmethod
    def c(msg, colour):
        try:
            from termcolor import colored, cprint
            p = lambda x : cprint(x, '%s' % colour)
            return p(msg)
        except:
            print(msg)

    @staticmethod
    def show_verbose(msg):
        colour.c(msg, 'white')

    @staticmethod
    def show_debug(msg):
        colour.c(msg, 'blue')

    @staticmethod
    def show_info(msg):
        colour.c(msg, 'green')

    @staticmethod
    def show_warn(msg):
        colour.c(msg, 'yellow')

    @staticmethod
    def show_error(msg):
        colour.c(msg, 'red')

class Logging:
    flag = True

    @staticmethod
    def error(msg):
        if Logging.flag == True:
            colour.show_error(get_now_time() + " [Error]:" + "".join(msg))

    @staticmethod
    def warn(msg):
        if Logging.flag == True:
            colour.show_warn(get_now_time() + " [Warn]:" + "".join(msg))

    @staticmethod
    def info(msg):
        if Logging.flag == True:
            colour.show_info(get_now_time() + " [Info]:" + "".join(msg))

    @staticmethod
    def debug(msg):
        if Logging.flag == True:
            colour.show_debug(get_now_time() + " [Debug]:" + "".join(msg))

    @staticmethod
    def success(msg):
        if Logging.flag == True:
            colour.show_verbose(get_now_time() + " [Success]:" + "".join(msg))


if __name__ == '__main__':

    info = '这是一条调试信息'
    Logging.error(u"测试一下")
    Logging.info("输出调试信息")
    Logging.info("输出info：%s" % info)

    @l()
    def lTest():
        Logging.success("测试成功")

    lTest()