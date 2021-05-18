#! /root/anaconda3/bin/python
import sys
"""
   如果一个类对象实现了特殊方法__enter__()和__exit__(),那么就称这个类对象遵守了上下文管理协议，这个类对象的实例对象被称为上下文管理器。
"""


class MyContextManager(object):
    def __enter__(self):
        print("特殊方法__enter__()被调用了")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("特殊方法__exit__()被调用了")
        print('异常的类型： %s' % exc_type)
        print('异常的错误信息：%s' % exc_val)
        print('异常调用堆栈的跟踪信息：%s' % exc_tb)
        # return True

    def do_sth(self):
        print("方法do_sth()被调用")
        print(1 / 0)


# with MyContextManager() as mcm:
#    mcm.do_sth()

"""
1）计算上下文表达式MyContextManager() 返回这个上下文管理器 并创建运行这个上下文
2）进入运行时上下文，自动调用上下文管理器的特殊方法__enter__(),[将特殊方法__enter__()的return self MyContextManager() == mcm]
3）如果with语句体产生异常那么__exit__ return true会继续执行下去，否者不会执行下去, 或者使用捕获过滤器
"""
try:
    with MyContextManager as mcm:
        mcm.do_sth()
except Exception:
    ex_type, ex_value, ex_traceback = sys.exc_info()

    print('异常的类型: %s' % ex_type)
    print('异常的错误信息：%s' % ex_value)
    print('异常调用堆栈的跟踪信息：%s' % ex_traceback)
