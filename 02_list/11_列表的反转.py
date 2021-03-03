#! /root/anaconda3/bin/python
L = [1, 2, 3, 4, 5]
L.reverse()
print(L)

L = [1, 2, 3, 4, 5]
iterator = reversed(L)
print('next', next(iterator))
print('next', next(iterator))
print('next', next(iterator))
print('next', next(iterator))
print('next', next(iterator))

print()

iterator = reversed(L)
print(iterator)
print(list(iterator))
print(L)
