#! /root/anaconda3/bin/python
from functools import partial


# 例子一
def f1(a, b=5, *args, **kwargs):
    print("a={}, b={}, args={}, kwargs={}".format(a, b, args, kwargs))


f1_new = partial(f1, 1, 3, 6, m=8)
f1_new()
f1_new(2, 4, n=9)


# 例子二
def f2(a, b=5, *, c, **kwargs):
    print("a={}, b={}, c={}, kwargs={}".format(a, b, c, kwargs))


f2_new = partial(f2, 1, m=8)
try:
    f2_new()
except Exception as err:
    print(type(err))
    print(err)
f2_new(3, c=9)
