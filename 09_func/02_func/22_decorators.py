#! /root/anaconda3/bin/python

"""
如果希望被装饰函数的特殊属性__name__的值为其函数名，而不是装饰器的内函数的函数名，可以在装饰器的内函数前面添加另外一个装饰器：@functools.wraps(装饰器的参数名)，其中functools.wraps指的是标准库模块functools中的函数wraps。
"""

from functools import wraps


def log3(month, day):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("%s%s,函数%s被调用了" % (month, day, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


"""
add3 = log3('6月', '18日')(add3)
log3('6月', '18日') -----> return decorator 内存地址
log3('6月', '18日')(add3) -----> return wrapper 内存地址

add3(1, 2) = log3('6月', '18日')(add3)(1, 2)
"""


@log3('6月', '18日')
def add3(sum1, sum2):
    print(sum1, sum2)
    return sum1 + sum2


print(add3(1, 2))
print(log3.__name__)
print(add3.__name__)

print('line(add3) total:', log3('6月', '18日')(add3).__closure__)
print('line(add3) first:', log3('6月', '18日')
      (add3).__closure__[0].cell_contents)
print('line(add3) second', log3('6月', '18日')
      (add3).__closure__[1].cell_contents)
print('line(add3) third', log3('6月', '18日')(add3).__closure__[2].cell_contents)

print('line(log3) total:', log3('6月', '18日').__closure__)
print('line(log3) first:', log3('6月', '18日').__closure__[0].cell_contents)
print('line(log3) second', log3('6月', '18日').__closure__[1].cell_contents)
