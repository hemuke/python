#! /root/anaconda3/bin/python
from functools import partial

# 例子一


def f(a, b=5):
    print("a: {}, b: {}".format(a, b))


f_new = partial(f, 2)
f_new()
f_new(b=6)
f_new(7)
try:
    f_new(a=4)
except TypeError as err:
    print(type(err))
    print(err)


# 例子二
def eval_sum(*args):
    s = 0
    print(args)
    for n in args:
        s += n
    return s


eval_sum_new = partial(eval_sum, 20, 30)
print(eval_sum_new(1, 2, 3, 4, 5))
