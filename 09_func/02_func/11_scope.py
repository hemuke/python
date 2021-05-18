#! /root/anaconda3/bin/python
# 例子一
g = 18


def f1():
    g = 19
    print(g)


f1()
print(g)


# 例子二
def f2():
    global g
    g = 20
    print(g)


f2()
print(g)


# 例子三
def f3():
    g += 1
    print(g)


try:
    f3()
except Exception as err:
    print(type(err))
    print(err)
