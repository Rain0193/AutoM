#!/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = "rain"

'''
：Python语言特点
    1.解释型脚本语言（高级数据结构）
    2.面向对象的语言（数据和逻辑相分离）
    3.不用考虑内存问题
    4.Python3.x 默认编码UTF-8. Python2.x 默认
'''

# 行与缩进
'''
代码块使用缩进进行区分，缩进的数量是可变的，建议采用 4 个空格
'''
def foo(age):           # 这是一个代码块
    if age > 18:
        print("Adult")
    else:
        print("Teenager")

# 多行语句
# 方式- 使用 \ 断行
'''
total = space_one + \
        space_two + \
        space_thre
'''

# 方式二 (),{},[]有隐式连接多行语句的功能，推荐
'''
total = (space_one +
         space_two +
         space_three)
'''
# 方式三 可以在一行中使用多条语句，用 ; 隔开，但不推荐这样做
print('a'); print('b')

print("Hello, World! 这是我的第一个Python程序。")

# 标识符
'''
1.由字母数字或_组成
2.不得以数字开头，不允许出现标点
3.严格区分大小写
'''

# 保留字
import keyword

print(keyword.kwlist)

keyword = ['False', 'None', 'True', 'and', 'as', 'assert', 'break',
           'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
           'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
           'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

if __name__ == "__main__":

    print("good good study, day day up")

    print("life is short, i like python")
