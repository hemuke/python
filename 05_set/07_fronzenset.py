#! /root/anaconda3/bin/python
# 不可变的set
print(frozenset())
print(frozenset(range(1, 6)))
print(frozenset([3, 5, 9, 2, 6]))
print(frozenset((3, 5, 9, 2, 6)))
print(frozenset({3, 5, 9, 2, 6}))
print(frozenset('35926'))
print(frozenset([3, 5, 9, 2, 6, (7, 8)]))
