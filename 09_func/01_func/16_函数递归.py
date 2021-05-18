#! /root/anaconda3/bin/python
from functools import reduce


def fib(n):

    print(reduce(lambda x, y: x * y, [i for i in range(1, n + 1)]))


fib(6)


def fac(n):
    """
    求阶乘递归
    """
    if n == 1:
        return 1
    return n * fac(n - 1)


print(fac(6))
print(fac.__doc__)


def fib1(n):
    """
    求指定位置的斐波那切数列的值
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)


print(fib1(6))


def fib2(m):
    """
    斐波那切数列求和
    """
    i = 0
    a = 0
    b = 1
    sum = 0
    while i <= m:
        print(a)
        sum += a
        a, b = b, a + b
        i += 1
    print("合", sum)


fib2(6)
