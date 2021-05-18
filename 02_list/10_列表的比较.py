#! /root/anaconda3/bin/python
print([2, 3, 8, 6, 7] < [2, 3, 9, 5, 1])
print([7, [2, 6]] > [7, [2, 5]])

a = b = [1, 2, 3]
c = [1, 2, 3]

print(a == b)
print(a == c)

print(a is b)
print(a is c)
