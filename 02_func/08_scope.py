#! /root/anaconda3/bin/python
# 例子一
def do_sth(a):
    print(a)
    b = 3
    print(b)


do_sth(3)

try:
    print(a)
except Exception as err:
    print(err)

try:
    print(b)
except Exception as err:
    print(err)


# 例子二
def outer():
    m = 5

    def inner():
        print(m)

    inner()


outer()
try:
    print(m)
except Exception as err:
    print(err)
