#! /root/anaconda3/bin/python
L = sorted([5, 3, 8, 1, 6])

print(L)

L.sort(reverse=True)
print(L)

###########################################

L = [5, 3, 8, 1, 6]

print(sorted(L))
print(L)

print(sorted(L, reverse=True))
print(L)

###########################################

L = [5, 3, 8, 1, 6]
iterator = iter(sorted(L))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
