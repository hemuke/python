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
