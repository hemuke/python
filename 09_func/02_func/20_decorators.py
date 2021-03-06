#! /root/anaconda3/bin/python

"""
如果希望被装饰函数的特殊属性__name__的值为其函数名，而不是装饰器的内函数的函数名，可以在装饰器的内函数前面添加另外一个装饰器：@functools.wraps(装饰器的参数名)，其中functools.wraps指的是标准库模块functools中的函数wraps。
"""

from functools import wraps


def log2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("函数%s被调用了" % func.__name__)
        #print(func(*args, **kwargs))
        return func(*args, **kwargs)
    return wrapper


@log2
# add2 = log2(add2)
# add2(1, 3) = log2(add2)(1, 3)
def add2(sum1, sum2):
    #print(sum1, sum2)
    return sum1 + sum2
    pass


print(add2(1, 3))
print(add2.__name__)
print(log2(add2).__closure__)
print(log2(add2).__closure__[0].cell_contents)
