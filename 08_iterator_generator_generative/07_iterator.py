#! /root/anaconda3/bin/python
from collections.abc import Iterable
from collections.abc import Iterator
"""
     @可以用于for-in语句的对象被称为可迭代对象。例如:range、列表、元组、字符串、字典、集合、生成器、都是可迭代对象
     @生成器也是迭代器
     @可以调用内置函数isinstance()判断一个对象是否是可迭代对象。
"""
print(isinstance([1, 2, 3], Iterable))
print(isinstance('abc', Iterable))
print(isinstance((i * i for i in range(1, 7)), Iterable))

"""
     @如果一个可迭代对象可以作为内置函数next()的实参从而支持惰性推算，那么该对象被称为迭代器(Iterator)对象。
     @对于range、列表、元组、字符串、字典和集合等可迭代对象，都不可以作为内置函数next()的实参，而生成器可以。所以，生成器是迭代器的一种。
"""
L = [1, 2, 3]
# next(L)
s = 'abc'
# next(s)
t = (1, 2, 3)
# next(t)

print(isinstance(L, Iterator))
print(isinstance(s, Iterator))
print(isinstance(t, Iterator))
print(isinstance((i * i for i in range(1, 8)), Iterator))

iter_L = iter(L)
iter_s = iter(s)

print(isinstance(iter_L, Iterator))
print(isinstance(iter_s, Iterator))

print(next(iter_L))
print(next(iter_s))
