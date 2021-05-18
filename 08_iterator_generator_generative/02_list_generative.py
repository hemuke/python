#! /root/anaconda3/bin/python
L = []
for i in range(1, 7):
    L.append(i * i)
print("例子一，方法一：", L)

L = [i * i for i in range(1, 7)]
print("例子一，方法二：", L)
print()
############################################################################
L = []
for i in range(1, 7):
    if not i % 2:
        L.append(i * i)
print("例子二，方法一：", L)

L = [i * i for i in range(1, 7) if not i % 2]
print("例子二，方法二：", L)
print()
############################################################################
L = []
for i in range(1, 4):
    for j in range(1, 4):
        L.append((i, j))
print("例子三，方法一：", L)

L = [(i, j) for i in range(1, 4) for j in range(1, 4)]
print("例子三，方法二：", L)
print()
############################################################################
L = []
for i in range(1, 4):
    if i != j:
        for j in range(1, 4):
            L.append((i, j))
print("例子四，方法一 不对：", L)


L = []
for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            L.append((i, j))
print("例子四，方法二 对：", L)

L = [(i, j) for i in range(1, 4) for j in range(1, 4) if i != j]
print("例子四，方法三 对：", L)
print()
###########################################################################
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

s = []
for i in range(4):
    L = []
    for j in matrix:
        L.append(j[i])
    s.append(L)
print("例子五，方法一：", s)

L = [[j[i] for j in matrix] for i in range(4)]
print("例子五，方法二：", L)
