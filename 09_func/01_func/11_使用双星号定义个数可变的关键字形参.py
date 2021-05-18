#! /root/anaconda3/bin/python
def f(**kwargs):
    print(kwargs)


f()
f(a=1)
f(a=1, b=2, c=3)


'''
定义函数时，最多只能定义一个个数可变的关键字形参
很多内置函数都定义了个数可变的关键字形参。例如，内置函数sorted()的定义为：
def sorted(*args, **kwargs):
'''


L = ['Python', 'Java', 'Swift']
print(sorted(L))
print(sorted(L, key=len))
print(sorted(L, key=len, reverse=True))


def fun(*args, **kwargs):
    print(kwargs, args)
