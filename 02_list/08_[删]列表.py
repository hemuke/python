#! /root/anaconda3/bin/python
L = [3, 4, 5, 6, 7]

L.remove(4)

L.remove(5)

print(L)

try:
    L.remove(9)
except Exception:
    print(Exception)

print()
####################################
L = [3, 4, 5, 6, 7]

L.pop(2)
print(L)

try:
    L.pop(8)
except Exception:
    print(Exception)

L.pop()
print(L)
####################################
L = [3, 4, 5, 6, 7, 8, 9]

L[2:3] = []
print(L)

L[1:4] = []
print(L)

L[:] = []
print(L)
####################################
L = [3, 4, 5, 6, 7, 8, 9]

del L[2]
print(L)

del L[1:4]
print(L)
####################################
L = [3, 4, 5, 6, 7, 8, 9]

L.clear()
print(L)
####################################
L = [3, 4, 5, 6, 7, 8, 9]
L[2:2] = []

print(L)
