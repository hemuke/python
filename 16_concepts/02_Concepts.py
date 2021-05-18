"""
############################
#1)掌握赋值语句内存分析方法"
#2)掌握id()和is使用方法    "
#3)了解python的垃圾回收机制"
#4)了解python的内存管理机制"
############################
"""


def extend_list(val, l=[]):
    print("-----------------------")
    print(l, id(l))
    l.append(val)
    print(l, id(l))
    return l


list1 = extend_list(10)
print(list1)
list2 = extend_list(123, [])
print(list2)
list3 = extend_list('a')
print(list3)

print(list1)
print(list2)
print(list3)
