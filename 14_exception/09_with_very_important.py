#! /root/anaconda3/bin/python

"""
   如果一个类对象实现了特殊方法__enter__()和__exit__(),那么就称这个类对象遵守了上下文管理协议，这个类对象的实例对象被称为上下文管理器。
"""


class MyContextManager(object):
    def __enter__(self):
        print("特殊方法__enter__()被调用了")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("特殊方法__exit__()被调用了")

    def do_sth(self):
        print("方法do_sth()被调用")

with MyContextManager() as mcm:
    mcm.do_sth()

"""
1）计算上下文表达式MyContextManager() 返回这个上下文管理器 并创建运行这个上下文
2）进入运行时上下文，自动调用上下文管理器的特殊方法__enter__(),[将特殊方法__enter__()的return self MyContextManager() == mcm]
3）with语句不报错 直接调用__exit__语句
"""
