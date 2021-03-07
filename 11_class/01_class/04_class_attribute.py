#! /root/anaconda3/bin/python
class MyClass(object):
    cal1 = 18

    def do_sth(self):
        print(MyClass.cal1)

    def do_another(self):
        print(MyClass.cal2)


mc = MyClass()

mc.do_sth()

print(MyClass.cal1)
print(mc.cal1)

MyClass.cal2 = 56
print(MyClass.cal2)
print(mc.cal2)

MyClass.cal2 = 73
print(MyClass.cal2)
print(mc.cal2)

mc.do_another()

"""
    @访问实例属性和类属性都可以通过"实例对象.属性名"方式。当通过"实例对象.属性名"的方式访问属性时，会先查找指定的实例对象中有没有指定名称的实例属性，如果没有，再查找对应的类对象中有没有指定名称的类属性
"""
