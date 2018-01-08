# -*- coding: UTF-8 -*-
import selenium.common.exceptions
import time

from util.logger import Log

__author__ = 'rain'

'''
appium 基础操作方法封装
appium python api 参考：https://testerhome.com/topics/3711
'''
from selenium.webdriver.support.ui import WebDriverWait

class Element():
    def __init__(self, driver=''):
        self.driver = driver
        self.log = Log(self)

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except selenium.common.exceptions.NoSuchElementException:
            self.log.mylogger('Can not find element: %s' % loc[1], flag=2)
            raise
        except selenium.common.exceptions.TimeoutException:
            self.log.mylogger('Can not find element: %s' % loc[1], flag=2)
            raise

    def find_elements(self, *loc, index=None):
        '''
        查找一组元素中的一个元素
        :param loc: 定位器
        :param index: index = None则查找唯一元素，index != None 则根据索引查找元素
        :return:
        '''
        try:
            if index is not None:
                WebDriverWait(self.driver, 30).until(lambda driver: driver.find_elements(*loc))
                return self.driver.find_elements(*loc)[index]
            else:
                WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element(*loc).is_displayed())
                return self.driver.find_element(*loc)

        except selenium.common.exceptions.NoSuchElementException:
            self.log.mylogger('Can not find element: %s' % loc[1], flag=2)
            raise
        except selenium.common.exceptions.TimeoutException:
            self.log.mylogger('Can not find element: %s' % loc[1], flag=2)
            raise

    def click(self, loc):
        '''
        点击一个找到的单个个元素
        :param loc:
        :return:
        '''
        self.log.mylogger('Click element by %s: %s...' % (loc[0], loc[1]), flag=0)
        try:
            self.find_element(*loc).click()
        except AttributeError as e:
            raise e

    def clicks(self, loc, index=None):
        '''
        点击找到的控件的子控件
        :param loc:
        :param index:
        :return:
        '''
        self.log.mylogger('Click element by %s: %s...' % (loc[0], loc[1]), flag=0)
        try:
            self.find_elements(*loc)[index].click()
            time.sleep(1)
        except AttributeError as e:
            raise e

    def click_back(self):
        '''
        点击物理返回键
        :return:
        '''
        self.log.mylogger('Click device back key')
        self.driver.keyevent(4)
        time.sleep(1)

    def send_key(self, loc, text):
        try:
            self.log.mylogger('Clear input-box: %s...' % loc[1], flag=0)
            self.find_element(*loc).clear()
            time.sleep(1)
            self.log.mylogger('Input text:  %s' % text, flag=0)
            self.find_element(*loc).send_keys(text)
        except AttributeError as e:
            raise e

    def send_keys(self, loc, text, clear_first=True, click_first=True, index=None):
