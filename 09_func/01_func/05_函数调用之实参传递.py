#! /root/anaconda3/bin/python


# 例子一
'''
函数调用之前的: i = 10, L = [1, 2, 3]
初始化形参前: arg1 = 10, arg2 = [1, 2, 3]
初始化形参后: arg1 = 20, arg2 = [1, 2, 3, 4]
函数调用之后的: i = 10, L = [1, 2, 3, 4]
'''


def f(arg1, arg2):
    print("初始化形参前: arg1 = {}, arg2 = {}".format(arg1, arg2))
    arg1 = arg1 * 2
    arg2.append(4)
    print("初始化形参后: arg1 = {}, arg2 = {}".format(arg1, arg2))


i = 10
L = [1, 2, 3]
print("函数调用之前的: i = {}, L = {}".format(i, L))

f(i, L)
print("函数调用之后的: i = {}, L = {}".format(i, L))
print()

# 例子二
'''
函数调用之前的: i = 10, L = [1, 2, 3]
初始化形参前: arg1 = 10, arg2 = [1, 2, 3]
初始化形参后: arg1 = 20, arg2 = [1, 2, 3, 4]
函数调用之后的: i = 10, L = [1, 2, 3]
'''


def f(arg1, arg2):
    print("初始化形参前: arg1 = {}, arg2 = {}".format(arg1, arg2))
    arg1 = arg1 * 2
    arg2.append(4)
    print("初始化形参后: arg1 = {}, arg2 = {}".format(arg1, arg2))


i = 10
L = [1, 2, 3]
print("函数调用之前的: i = {}, L = {}".format(i, L))

f(i, L[:])
print("函数调用之后的: i = {}, L = {}".format(i, L))
