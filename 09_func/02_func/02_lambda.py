#! /root/anaconda3/bin/python
from collections.abc import Iterator
from collections.abc import Iterable
# 例子一


def add(num1, num2):
    return num1 + num2


print(add(1, 2))
print((lambda num1, num2: num1 + num2)(3, 4))

# 例子二


def le(num1, num2): return num1 + num2


print(le(5, 6))

# 例子三
result = map(lambda x: x * x, [1, 2, 3])
print(next(result))
print(next(result))
print(next(result))
print(result)
print(isinstance(result, Iterator))
print(isinstance(result, Iterable))


result = map(lambda x: x * x, [1, 2, 3])
print(list(result))

# 例子四


def do_sth():
    return lambda num1, num2: num1 + num2


print(do_sth()(7, 8))
