#! /root/anaconda3/bin/python

class MyException(Exception):
    def __init__(self, msg1, msg2):
        self.msg1 = msg1
        self.msg2 = msg2


print(MyException('Test1', 'Test2').msg1, MyException('Test1', 'Test2').msg2)
# 这个Exception 本身实现了打印
print(MyException('Test1', 'Test2'))

try:
    raise MyException("123", "abc")
except Exception:
    print(Exception)

print()


try:
    raise MyException("123", "abc")
except MyException as err:
    print(err)

my = MyException("a", "b")
print(my)


##########################################################################
class MyException2(object):
    def __init__(self, msg1, msg2):
        self.msg1 = msg1
        self.msg2 = msg2


print(MyException2("MyException2-1", "MyException2-2").msg1)
print(MyException2("MyException2-1", "MyException2-2"))
