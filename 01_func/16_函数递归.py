#! /root/anaconda3/bin/python


def fac(n):
    """ 
    阶乘递归
    """
    if n == 1:
        return 1
    return n * fac(n - 1)


print(fac(6))
print(fac.__doc__)


def fib(n):
    """ 
    斐波那切数列
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fac(4))
