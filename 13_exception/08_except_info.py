#! /root/anaconda3/bin/python

"""
标准库模块sys中的函数exc_info以获取异常的相关信息

异常的类型: <class 'ZeroDivisionError'>
异常的错误信息：division by zero
异常调用堆栈的跟踪信息：<traceback object at 0x7f689cbf5180>


提取Traceback对象中包含的信息，调用标准库traceback中的函数extract_tb()

[<FrameSummary file ./08_except_info.py, line 11 in f2>, <FrameSummary file ./08_except_info.py, line 7 in f1>]
文件名：./08_except_info.py
行数：11
函数名：f2
源码：f1()
文件名：./08_except_info.py
行数：7
函数名：f1
源码：print(1 / 0)
"""

import sys
import traceback


def f1():
    print(1 / 0)


def f2():
    try:
        f1()
    except ZeroDivisionError:
        ex_type, ex_value, ex_traceback = sys.exc_info()

        print('异常的类型: %s' % ex_type)
        print('异常的错误信息：%s' % ex_value)
        print('异常调用堆栈的跟踪信息：%s' % ex_traceback)

        tb = traceback.extract_tb(ex_traceback)
        print(tb)

        for filename, linenum, funcname, source in tb:
            print('文件名：%s' % filename)
            print('行数：%s' % linenum)
            print('函数名：%s' % funcname)
            print('源码：%s' % source)


f2()
