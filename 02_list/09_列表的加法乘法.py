#! /root/anaconda3/bin/python
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
print(L3)
print(L1)
print(L2)


L1 = L2 = [1, 2]
L1 = L1 + [3, 4]
print(L1, L2)

L1 = L2 = [1, 2]
L1 += [3, 4]
print(L1, L2)

L1 = [1, 2, 3]
L = L1 * 3
print(L)
print(L1)

L = [0] * 5
print(L)

L1 = L2 = [1, 2]
L1 = L1 * 3
print(L1, L2)

L1 = L2 = [1, 2]
L1 *= 3
print(L1, L2)
