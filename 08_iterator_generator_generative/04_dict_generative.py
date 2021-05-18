#! /root/anaconda3/bin/python
"""
    @什么是字典生成式
    @items = ['Fruits', 'Books', 'Others']
    @prices = [96, 78, 83]
"""
from collections.abc import Iterable
from collections.abc import Iterator


items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 83]
i = zip(items, prices)  # 迭代器
print(i)  # <zip object at 0x7f826e1a3fc0>
print(type(i))  # <class 'zip'>
print(isinstance(i, Iterable))  # True
print(isinstance(i, Iterator))  # True
print(next(i))
print(next(i))
print(next(i))

d = {}
for item, price in zip(items, prices):
    d[item.upper()] = price
print('例子一，方法一：', d)

d = {item.upper(): price for item, price in zip(items, prices)}
print('例子一，方法二：', d)

d = {item.upper(): price for item, price in zip(items, prices) if price > 80}
print('例子一，方法三：', d)
##############################################################################
d = {i: j for i in range(1, 4) for j in range(1, 4)}
print('例子二，方法一：', d)

d = {}
for i in range(1, 4):
    for j in range(1, 4):
        d[i] = j
print('例子二，方法二：', d)

d = {i: j for i in range(1, 4) for j in range(1, 4) if i != j}
print('例子二，方法三：', d)
