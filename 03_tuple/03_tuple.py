#! /root/anaconda3/bin/python
[a, b] = [5, 8]
print(a, b)

a, b = 5, 8
print(a, b)

a, *b, c = 1, 2, 3, 4
print(a, b, c)

a, b, *c = 1, 2, 3, 4
print(a, b, c)

*a, b, c = 1, 2, 3, 4
print(a, b, c)

a, *b, c = 1, 2, 3, 4
print(a, b, c)
