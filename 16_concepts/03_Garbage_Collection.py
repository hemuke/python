"""
# 垃圾回收机制
# 以引用计数为主，分代收集为辅

# 如果一个对象的引用数为0，Python虚拟机就会回收这个对象的内存

# 引用计数的缺陷是循环引用的问题

"""


class ClassGc():
    def __init__(self):
        print("对象产生：{0}".format(id(self)))

    def __del__(self):
        print("对象删除：{0}".format(id(self)))


def f0():
    """
    对象产生后，马上删除，引用由1变为0，内存被回收
    """
    while True:
        c1 = ClassGc()


def f1():
    """
    死循环，引用一直在用，无法回收
    """
    l = []
    while True:
        c1 = ClassGc()
        l.append(c1)
        print(len(l))


if __name__ == "__main__":
    f0()
# f1()
