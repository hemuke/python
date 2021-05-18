#! /root/anaconda3/bin/python
# 例子一
g = [1]


def f1():
    g = [2]
    print(g)


f1()
print(g)

# 例子二


def f2():
    g[0] = 2
    print(g)


f2()
print(g)
