#! /root/anaconda3/bin/python
L = [[3, 4], [1, 5, 2], [6, 8, 9, 7]]

print(L[2][1])

L[1] = 9
print(L)

L.append([2, 0])
print(L)

L.pop(2)
print(L)

##############################################
print([[0] * 3] * 4)
print([[0] * 3 for j in range(4)])
print([[0 for i in range(3)] for j in range(4)])
