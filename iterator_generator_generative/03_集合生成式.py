#! /root/anaconda3/bin/python
# 这个元祖一个元素必须要加逗号
s = set()
for i in range(1, 7):
    s.add((i * i,))
print("例子一，方法一:", s)

s = {(i * i,) for i in range(1, 7)}
print("例子一，方法二:", s)
print()
##########################################################
s = set()
for i in range(1, 7):
    s.add(i * i)
print("例子二，方法一:", s)

s = {i * i for i in range(1, 7)}
print("例子二，方法二:", s)
print()
##########################################################
s = set()
for i in range(1, 7):
    if not i % 2:
        s.add(i * i)
print("例子三，方法一:", s)

s = {i * i for i in range(1, 7) if not i % 2}
print("例子三，方法二:", s)
print()
##########################################################
s = set()
for i in range(1, 4):
    for j in range(1, 4):
        s.add((i, j))
print("例子四，方法一：", s)

s = {(i, j) for i in range(1, 4) for j in range(1, 4)}
print("例子四，方法二：", s)
