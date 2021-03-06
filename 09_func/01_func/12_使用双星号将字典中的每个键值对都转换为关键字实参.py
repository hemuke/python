#! /root/anaconda3/bin/python
def f(a, b, c):
    print('a = {}, b = {}, c = {}'.format(a, b, c))


f(a=1, b=1, c=2)
d = {'a': 1, 'b': 2, 'c': 3}

f(a=d['a'], b=d['b'], c=d['c'])
f(**d)
d1 = {'d': 1, 'e': 2, 'f': 3}

try:
    f(**d1)
except Exception as err:
    print(err)
    print(type(err))


def fun(**kwargs):
    print(kwargs)


fun(**d1)
