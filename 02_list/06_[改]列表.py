#! /root/anaconda3/bin/python

L = [3, 4, 5, 6, 7]

L[2] = 8
print(L)

L[1:4] = [1, 9, 2]
print(L)

L[1:2] = [5]
print(L)

L[1:4] = [1, 8]
print(L)
