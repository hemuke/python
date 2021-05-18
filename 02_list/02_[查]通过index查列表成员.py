#! /root/anaconda3/bin/python
L = [5, 3, 9, 4, 0, 6, 8, 1, 7, 2]

print(L[0])
print(L[-10])

print(L[6])
print(L[-4])

try:
    print(L[10])
except IndexError:
    print(IndexError)

print(L[9])
print(L[-1])
