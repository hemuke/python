#! /root/anaconda3/bin/python

L = [5, 3, 9, 4, 0, 6, 8, 1, 7, 2]

print(L[1:7:2])

print(L[1:7:])
print(L[1:7])

print(L[::])

print(L[::-1])
print(L[6:0:-2])
print(L[0:6:-2])
print(L[6::-2])
print(L[:5:-2])

# 切片操作是可以越界的
print(L[:100])
print(L[-100:])

#################################################
L = [5, 3, 9, 4, 0, 6, 8, 1, 7, 2]

print(L[1:7:2])
print(L[slice(1, 7, 2)])


