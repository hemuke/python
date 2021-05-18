#! /root/anaconda3/bin/python
t = (1, 2, 3, 4, 5)
del t

try:
    print(t)
except NameError:
    print(NameError)
