#! /root/anaconda3/bin/python
def f(a, b, *, c, d):
    print('a = {}, b = {}, c = {}, d = {}'.format(a, b, c, d))


f(1, 2, d=6, c=3)
