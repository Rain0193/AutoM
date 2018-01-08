# -*- coding: UTF-8 -*-
__author__ = 'rain'

import logging
import logging.config

'''
问题：如何在脚本和程序中将诊断信息写入文件，在终端输出
解决：使用logging模块
参考：https://gamelife1314.github.io/2017/03/09/Python-loggin%E5%86%85%E5%BB%BA%E6%97%A5%E5%BF%97%E6%A8%A1%E5%9D%97/
     http://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p11_add_logging_to_simple_scripts.html
     http://yshblog.com/blog/125
'''

# 硬编码方式配置日志
def main():
    # 配置日志 将错误输出到文件app.log中，只输出日志等级高于ERROR的信息
    # logging.basicConfig(filename='app.log', level=logging.ERROR) # level参数是一个过滤器，低于此级别的日志消息都会被忽略掉

    # 改变日志输出等级
    # logging.basicConfig(filename='app1.log',
    #                     level=logging.WARNING,
    #                     format='%(levelname)s:%(asctime)s:%(message)s')  # format参数格式化输出日志信息形式
    logging.basicConfig(filename='app1.log',
                        level=logging.DEBUG,
                        filemode='w',
                        format='%(asctime)s:%(filename)s:[line:%(lineno)d]:%(levelname)s:%(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S')

    # 输出日志到标准错误中, 不传filename
    # logging.basicConfig(level=logging.INFO)

    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'
    # 调用log输出等级 critical erro warning info 等级按降序排序
    logging.critical('Host %s unknown', hostname)
    logging.error("couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)

# 配置文件配置
def main2():
    logging.config.fileConfig('logconfig.ini')
    # logging.basicConfig(level=logging.INFO)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'
    # 调用log输出等级 critical erro warning info 等级按降序排序
    logging.critical('Host %s unknown', hostname)
    logging.error("couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)

if __name__ == '__main__':
    main()
    main2()
