#! /root/anaconda3/bin/python
def f1(a, b=5, *args, **kwargs):
    print('a = {}, b = {}, args = {}, kwargs = {}'.format(a, b, args, kwargs))


f1(2, 6, 7, 8, c=9)
f1(2)


def f2(a, b=6, *, c, **kwargs):
    print('a = {}, b = {}, c = {}, kwargs = {}'.format(a, b, c, kwargs))


f2(*(3, 7), **{'c': 8, 'd': 10})
f2(*(3, 7), c=7, **{'e': 8, 'd': 10})
f2(3, c=8, d=10)
