#! /root/anaconda3/bin/python

class MyException(Exception):
    def __init__(self, msg1, msg2):
        self.msg1 = msg1
        self.msg2 = msg2


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
