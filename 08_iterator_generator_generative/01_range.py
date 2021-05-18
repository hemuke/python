#! /root/anaconda3/bin/python
'''
    @range是一种序列类型，range类型用于表示不可变的整数序列
    @可以调用内置函数range(类range的构造方法)创建range类型的对象
    @内置函数range的返回值是一个迭代器对象
    @不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的
'''

print(range(5))
'''
    @next(range(5))报错是因为class range 只定义了__iter__,但是没有__next__特殊方法
'''
print(list(range(5)))
print(list(range(0, 5, 1)))

print(list(range(1, 5)))
print(list(range(1, 5, 1)))

print(list(range(0, 20, 4)))

print(list(range(0, -20, -4)))

print(3 in range(5))
print(8 not in range(5))
