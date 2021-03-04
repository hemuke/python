#! /root/anaconda3/bin/python
"""
     @集合中不可以存储重复的数据
     @集合中的数据是无序的
     @集合中的数据可以是任何不可变的类型
"""
s = {3, 5, 9, 2, 6}
print(s)

s = {3, 3, 3, 3}
print(s)

print(type({}))
print(type(set()))

print(set(range(1, 6)))
print(set([3, 5, 9, 2, 6]))
print(set((3, 5, 9, 2, 6)))
print(set({3, 5, 9, 2, 6}))
print(set('35926'))

print(set([3, 5, 3, 9, 2, 9, 3, 6]))
