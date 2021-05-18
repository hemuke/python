"""
####
# 以引用计数为主，分代收集为辅
# 如果一个对象的引用数为0,Python虚拟机就会回收这个对象的内存
# 引用计数的缺陷是循环引用的问题


# 每个对象都有存有指向该对象的引用总数
# 查看某个对象的引用计算
  # sys.getrefcount()
# 可以使用del关键字删除某个引用
  # sys.getrefcount()
####
"""
import sys
l = []

print(sys.getrefcount(l))
# 为什么结果是2 不是1,因为getrefcount()调用函数的时候也加了一次引用

l2 = l
l3 = l
print(sys.getrefcount(l))  # 4

l5 = l3
print(sys.getrefcount(l))  # 5

del l2
print(sys.getrefcount(l))  # 4

i = 132223
print("这个是对象不是引用", sys.getrefcount(i))
# 如果不是引用，是对象，是会随机产生一个值的，这个是共享内存的机制
a = i
print("这个是对象不是引用", sys.getrefcount(i))
