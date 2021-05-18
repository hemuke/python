#! /root/anaconda3/bin/python

L = [5, 3, 7, 9, 2, 1, 7, 6]
print(L.index(9))

print(L.index(7))

try:
    print(L.index(8))
except ValueError:
    print(ValueError)

print(L.index(7, 3))
# list不能只指定结束索引
