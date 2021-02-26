#! /root/anaconda3/bin/python


def f(a, b, c):
    print("a = {}, b = {}, c = {}".format(a, b, c))


f(b=5, a=2, c=3)
f(a=2, b=6, c=4)
f(c=3, b=4, a=3)
f(2, 5, c=8)
