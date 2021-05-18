#! /root/anaconda3/bin/python
"""
    @实例属性的绑定
    @在类对象的内部(方法中)
        语法格式:self.属性名
    @在类对像的外部
        语法格式:实例对象.属性名
"""
# 例子1


class MyClass1(object):

    def __init__(self):
        self.ia1 = 1

    def do_sth1(self):
        print(self.ia1)


mc = MyClass1()
print(mc.ia1)
mc.do_sth1()
print()

# 例子2


class MyClass2(object):

    def do_another(self):
        self.ia2 = 2

    def do_sth2(self):
        print(self.ia2)


try:
    MyClass2().do_sth2()
except Exception:
    print(Exception)

mc2 = MyClass2()
mc2.do_another()
mc2.do_sth2()
print()
"""
MyClass2().do_another()
MyClass1().do_sth2()
实例没保存
"""


# 例子3
class MyClass3(object):
    def do_sth3(self):
        print(self.ia3)


mc = MyClass3()
mc.ia3 = 3
print(mc.ia3)
mc.ia3 = 4
print(mc.ia3)
mc.do_sth3()

""
# 同一个类对象的不同实例对象所绑定的实例属性是相互独立的。也就是说，给一个实例对象所绑定的实例属性，对于另外一个实例对象是不起作用的
""
mc2 = MyClass3()
try:
    mc2.do_sth3()
except AttributeError:
    print(AttributeError)

# 例子四


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


s1 = Student('张三', 98)
s2 = Student('李四', 86)

s1.age = 18
# 访问特殊属性__dict__可以获得实例对象所绑定的所有属性和方法的字典
print(s1.__dict__)
print(s2.__dict__)
