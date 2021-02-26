#! /root/anaconda3/bin/python


def f1(a, b=5):
    print('a = {}, b = {}'.format(a, b))


f1(2, 6)
f1(2)


def f2(a, b=5, c=8):
    print('a = {}, b = {}, c = {}'.format(a, b, c))


f2(2, 6, 9)
f2(2)
f2(2, 6)
f2(2, c=9)


def fun1(L=[]):
    L.append(18)
    print(L)


fun1()
fun1()
fun1()
fun1()


def fun2(L=None):
    if L is None:
        L = []
    L.append(18)
    print(L)


fun2()
fun2()
fun2()
fun2()
fun2()
