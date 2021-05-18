#! /root/anaconda3/bin/python

# 例子一 内置函数locals()可以返回其所在局部作用域的命名空间
def outer1(a):
    b = 8

    def inner(c):
        d = 3
        print(locals())

    return inner


outer1(5)(2)
print(outer1.__closure__[0])
# {'c': 2, 'd': 3}

# 例子二 内置函数locals()可以返回其所在局部作用域的命名空间


def outer2(a):
    b = 8

    def inner(c):
        d = 3
    print(locals())


outer2(5)
# {'a': 5, 'b': 8, 'inner': <function outer.<locals>.inner at 0x7fe8745081f0>}

g = 2


class MyClass(object):
    pass


print(globals())
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fde952df130>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': './13_locals_globals.py', '__cached__': None, 'outer': <function outer at 0x7fde8dcfbd30>, 'g': 2, 'MyClass': <class '__main__.MyClass'>}
