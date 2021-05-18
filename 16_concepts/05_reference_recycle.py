#! /root/anaconda3/bin/python
# 循环引用
import gc
import sys
import objgraph

print("查看gc.get_threshold信息:\t\t", gc.get_threshold())
# (700, 10, 10)
print()


class Person(object):
    pass


class Cat(object):
    pass


p = Person()  # class Person 引用了第1次
c = Cat()    # class Cat 引用了第1次
p.name = "Susan"  # 这个是class 类的实例属性不影响引用次数因为标记在p变量上
p.pet = c    # class Cat 引用了第2次
c.master = p  # class Person 引用了第2次

print("查看class Person的实例化p:\t\t", sys.getrefcount(p))  # 调用这个函数取查看也是一次引用
print(objgraph.count('Person'))
"""
p = Person() 第一次引用
c.master = p 第二次引用
sys.getrefcount(p) 第三次引用
"""
print("查看class Cat的实例化c:\t\t\t", sys.getrefcount(c))
print(objgraph.count('Cat'))
"""
c = cat()
p.pet = c
sys.getrefcount(c)
"""
print()

# 第一次手动回收
gc.collect()
print("第一次手动回收class Person:\t\t", objgraph.count('Person'))
print("第一次手动回收class Cat:\t\t", objgraph.count('Cat'))
# 记录当前类产生的实例对象的个数
print()

# 第二次手动回收
del p
del c

gc.collect()
print("第二次手动回收class Person:\t\t", objgraph.count('Person'))
print("第二次手动回收class Person:\t\t", objgraph.count('Cat'))
# 记录当前类产生的实例对象的个数
