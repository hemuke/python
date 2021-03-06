#! /root/anaconda3/bin/python


def f(a, b, c):
    print('a = {}, b = {}, c = {}'.format(a, b, c))


f(1, 2, 3)
L = [1, 2, 3]
f(L[0], L[1], L[2])
f(*L)

try:
    f(L)
except Exception as err:
    print(type(err))
    print(err)


def fun(*args):
    print("args = {}".format(args))


fun(L)
fun(*L)
