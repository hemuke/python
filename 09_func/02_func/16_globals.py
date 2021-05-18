#! /root/anaconda3/bin/python
"""
   globals()返回的是实际的命名空间，所以，对globals()所做的任何修改，其实就是对实际命名空间的修改。
"""
import time
g = 20

print(globals())

globals()['g'] = 6
globals()['gg'] = 66

print()
print(globals())

"""
    可以在局部作用域或嵌套作用域中通过globals()返回值，来访问全局作用域中被屏蔽的全局变量
"""


def do_sth():
    g = 123
    print(g)
    print(globals()['g'])
    print(vars())


print()
do_sth()

print(vars())
print(vars(time))
