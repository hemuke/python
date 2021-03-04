#! /root/anaconda3/bin/python
s = {3, 4, 5, 6, 7}
s.remove(5)
print(s)

try:
    s.remove(10)
except KeyError:
    print(KeyError)

s = {3, 4, 5, 6, 7}
s.discard(5)
print(s)
s.discard(19)
print(s)

s = {3, 4, 5, 6, 7}
print(s.pop())
print(s)

s = {3, 4, 5, 6, 7}
s.clear()
print(s)
