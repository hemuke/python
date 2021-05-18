#! /root/anaconda3/bin/python


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


foo(1)

"""
    @assert(condition)
    @if not condition:
        raise AssertionError()
"""

assert(1 == 1)
assert(5 > 1)
a = "hello"
b = "hello"
assert(a == b)

try:
    assert(1 > 100)
except AssertionError:
    print(AssertionError)

a = [0, 1, 2, 3, 4]
b = [0, 1, 2, 3, 4]
assert(a == b)
