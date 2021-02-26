#! /root/anaconda3/bin/python


def f(*args):
    print(args)


f()
f(1)
f(1, 2, 3)


'''
def print(self, *args, sep=' '. end='\n', file=None)
'''
print()
print(1)
print(1, 2)
print(1, 2, 3)


def fun1(a, b, *c):
    print('a = {}, b = {}, c = {}'.format(a, b, c))


fun1(1, 2, 3, 4, 5)


def fun2(a, *b, c, d):
    print('a = {}, b = {}, c = {}, d = {}'.format(a, b, c, d))


fun2(1, 2, 3, 4, c=5, d=6)
