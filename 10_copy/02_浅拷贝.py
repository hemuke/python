#! /root/anaconda3/bin/python
"""
    @对于没有嵌套对象的不可变对象，例如：整数对象、字符串对象和元组对象等，不会进行拷贝，也就是说不会创建另一对象
"""
import copy
i1 = 1811111111111111111111
i2 = int(i1)
i3 = copy.copy(i1)
print(id(i1) == id(i2))
print(id(i1) == id(i3))
print(id(i2) == id(i3))
print()


t1 = (1, 2, 3)
t2 = copy.copy(t1)
print(id(t1) == id(t2))
print()


"""
    @对于没有嵌套对象的不可变对象，例如：整数对象、字符串对象和元组对象等，不会进行拷贝，也就是说不会创建另一对象
"""
t3 = ([1, 2], 3, 4)
t4 = copy.copy(t3)
print(id(t3) == id(t4))  # True
print(id(t3[0]) == id(t4[0]))  # True
t3[0][0] = 2
print(t3, t4)
