#! /root/anaconda3/bin/python
"""
    @所谓浅拷贝，指的是：对于某个对象，虽然创建了与该对象具有相同值的另一个对象。但是，这两个对象内部嵌套的对应子对象全都是同一个对象。简单地说。外部进行了拷贝，内部没有拷贝。
    @以下方式得到拷贝都是浅拷贝:
    @1.切片操作[:]
    @2.调用列表、字典、集合的方法copy()
    @3.调用内置函数list()、dict()、set()
    @4.调用标准库模块copy中的函数copy()
"""
"""
    @对于没有嵌套对象的不可变对象，例如：整数对象、字符串对象和元组对象等，不会进行拷贝，也就是说不会创建另一对象
"""
"""
    @内置不可变对象 可变对象 引用的id都是一样的，但是不可变对象如果改变了 需要创建一个新的对象
"""


import copy
print("第一组信息")
L1 = [[3, 6], 8]
L2 = L1[:]
print(id(L1) == id(L2))  # False
print(id(L1[0]) == id(L2[0]))  # True
print(id(L1[1]) == id(L2[1]))  # True
print(id(L1[0][0]) == id(L2[0][0]))  # True
print(id(L1[0][1]) == id(L2[0][1]))  # True
L1[0][0] = 4
print(L1, L2)  # [[4, 6], 8] [[4, 6], 8]
L1[1] = 7
print(L1, L2)  # [[4, 6], 7] [[4, 6], 8]
print()


print("第二组信息")
L1 = [[3, 6], 8]
L2 = L1.copy()
print(id(L1) == id(L2))  # False
print(id(L1[0]) == id(L2[0]))  # True
print(id(L1[1]) == id(L2[1]))  # True
print(id(L1[0][0]) == id(L2[0][0]))  # True
print(id(L1[0][1]) == id(L2[0][1]))  # True
L1[0][0] = 4
print(L1, L2)  # [[4, 6], 8] [[4, 6], 8]
L1[1] = 7
print(L1, L2)  # [[4, 6], 7] [[4, 6], 8]
print()


print("第三组信息")
L1 = [[3, 6], 8]
L2 = list(L1)
print(id(L1) == id(L2))  # False
print(id(L1[0]) == id(L2[0]))  # True
print(id(L1[1]) == id(L2[1]))  # True
print(id(L1[0][0]) == id(L2[0][0]))  # True
print(id(L1[0][1]) == id(L2[0][1]))  # True
L1[0][0] = 4
print(L1, L2)  # [[4, 6], 8] [[4, 6], 8]
L1[1] = 7
print(L1, L2)  # [[4, 6], 7] [[4, 6], 8]
print()


print("第四组信息")
L1 = [[3, 6], 8]
L2 = copy.copy(L1)
print(id(L1) == id(L2))  # False
print(id(L1[0]) == id(L2[0]))  # True
print(id(L1[1]) == id(L2[1]))  # True
print(id(L1[0][0]) == id(L2[0][0]))  # True
print(id(L1[0][1]) == id(L2[0][1]))  # True
L1[0][0] = 4
print(L1, L2)  # [[4, 6], 8] [[4, 6], 8]
L1[1] = 7
print(L1, L2)  # [[4, 6], 7] [[4, 6], 8]
print()


print("第五组信息")
L1 = [[3, 6], {7, 8}]
L2 = copy.copy(L1)
print(id(L1) == id(L2))  # False
print(id(L1[0]) == id(L2[0]))  # True
print(id(L1[1]) == id(L2[1]))  # True
print(id(L1[0][0]) == id(L2[0][0]))  # True
print(id(L1[0][1]) == id(L2[0][1]))  # True
L1[0][0] = 4
print(L1, L2)  # [[4, 6], {8, 7}] [[4, 6], {8, 7}]
L1[1].add(9)
print(L1, L2)  # [[4, 6], {8, 9, 7}] [[4, 6], {8, 9, 7}]
print()


print("第六组信息")
L1 = [[3, 6], {7, 8}]
L2 = copy.copy(L1)
L1[1] = 7
print(L1, L2)  # [[3, 6], 7] [[3, 6], {8, 7}]
print()
