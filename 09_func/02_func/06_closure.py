#! /root/anaconda3/bin/python
# 例子一
def outer1():
    a = 10

    def inner():
        # nonlocal a
        a = 11
        print('例子一 内函数:', a)
        '''
        这里的a变量 已经替换掉了外函数的a变量，在PyCharm里面会报错因此不建议这么使用
        '''
    print('例子一 外函数:', a)
    return inner


outer1()()
print('例子一__closure__: #闭包值为None', outer1().__closure__)


# 例子二
def outer2():
    a = 10

    def inner1():
        a = 11
        print('例子二inner1:', a)

    inner1()

    def inner2():
        print('例子二inner2:', a)

    inner2()
    # return inner2


print()
outer2()
try:
    print("例子二__closure__:", outer2().__closure__)
except AttributeError as err:
    print("例子二__closure__, type(err):", type(err))
    print("例子二__closure__, err:", err)
# print("例子二__closure__[0].cell_contents", outer2().__closure__[0].cell_contents)


# 例子三


def outer3():
    a = [3]

    def inner3():
        a = [8]
        print("例子三 内函数:", a)
        '''
        这里的a变量 已经替换掉了外函数的a变量，在PyCharm里面会报错因此不建议这么使用
        '''
    print("例子三 外函数:", a)

    return inner3


print()
outer3()()
print("例子三__closure__:", outer3().__closure__)


# 例子四
def outer4():
    a = [3]

    def inner4():
        a[0] = 8
        print("例子四 内函数:", a)

    print("例子四 外函数:", a)
    return inner4


print()
outer4()()
print("例子四__closure__:", outer4().__closure__)
print("例子四__closure__[0].cell_contents:",
      outer4().__closure__[0].cell_contents)


# 例子四B
def outer4B():
    a = [3]

    def inner4():
        a[0] = 8
        print("例子四B 内函数:", a)
    inner4()

    print("例子四B 外函数:", a)


print()
outer4B()

# 例子四C
def outer4C():
    a = [3]

    def inner4():
        a[0] = 8
        print("例子四B 内函数:", a)
    inner4()

    print("例子四B 外函数:", a)
    return inner4


print()
outer4C()

try:
    print("例子二__closure__:", outer4C().__closure__)
except Exception as err:
    print("例子二__closure__, type(err):", type(err))
    print("例子二__closure__, err:", err)
print("例子二__closure__[0].cell_contents", outer4C().__closure__[0].cell_contents)


# 例子五
def outer5():
    a = 10

    def inner5():
        nonlocal a
        a += 1

        print("例子五，内函数:", a)

    print("例子五，内函数:", a)
    return inner5


print()
outer5()()
print("例子五__closure__:", outer5().__closure__)
print("例子五__closure__[0].cell_contents:",
      outer5().__closure__[0].cell_contents)
