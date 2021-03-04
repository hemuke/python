#! /root/anaconda3/bin/python
"""
    @修改函数，使之输入func_2能运行，并且输出结果为123
"""
#def func_1(a):
#    return a()
#
#def func_2():
#    return '123'
#
#b = input(">>")
#print(func_1(b))

def func_1(a):
    return a()

def func_2():
    return '123'

b = eval(input(">>"))
print(func_1(b))
