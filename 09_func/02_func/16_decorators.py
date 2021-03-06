#! /root/anaconda3/bin/python


def hi():
    return "hi yasoob!"


def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func)  # <function hi at 0x7f0ea36a61f0>
    print("func", func.__name__)  # hi


doSomethingBeforeHi(hi)

print()
print(hi.__name__)  # hi
print(doSomethingBeforeHi.__name__)  # doSomethingBeforeHi

# 函数.__name__指的是这个脚本正在执行时候用的函数

print(dir())
