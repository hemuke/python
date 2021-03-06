#! /root/anaconda3/bin/python

# 例子一 内置函数locals()可以返回其所在局部作用域的命名空间
"""
locals()并没有返回实际的命名空间，而是返回值的拷贝，所以通过locals()修改某个名字对应的值，对于实际的命名空间是没有影响的;但是,可以通过locals()向实际的命名空间中添加一个名字和值的映射。
"""


def f():
    x = 8
    print(locals())  # {'x': 8}

    locals()['x'] = 9
    locals()['y'] = 10

    print(locals())  # {'x': 8, 'y': 10}


f()
