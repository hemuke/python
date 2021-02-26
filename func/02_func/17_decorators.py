#! /root/anaconda3/bin/python


def hi():
    return "hi yasoob!"
 
def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func)
 
doSomethingBeforeHi(hi)
