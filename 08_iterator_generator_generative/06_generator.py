#! /root/anaconda3/bin/python
import sys
"""
    @上面使用类似生成式的语法得到的生成器被称为生成器表达式。
    @使用生成器函数得到生成器。
    @生成器函数中通过关键字yield返回推算出的元素。生成器函数与普通函数的区别在于：当调用内置函数next()或使用for-in语句进行迭代时，执行完yield语句就会生成器函数挂起，下次会从挂起的地方继续执行。
"""


def fib(n):
    i = 0
    a, b = 1, 1
    while i < n:
        yield a
        a, b = b, a + b
        i += 1


gf = fib(6)
print(gf)

print(next(gf))
print(next(gf))
print(next(gf))
print(next(gf))
print(next(gf))
print(next(gf))
try:
    print(next(gf))
except Exception:
    ex_type, ex_value, ex_traceback = sys.exc_info()

    print('异常的类型: %s' % ex_type)
    print('异常的错误信息：%s' % ex_value)
    print('异常调用堆栈的跟踪信息：%s' % ex_traceback)

gf = fib(6)

for item in gf:
    print(item)
print("*********************************************")
print(item)
