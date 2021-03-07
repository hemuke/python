#! /root/anaconda3/bin/python
def a_line(a, b):

    def arg_y(y):
        return a * x + b

    return arg_y


line1 = a_line(3, 5)
line2 = a_line(5, 10)
print(line1(10))
print(line1(20))


def a_line(a, b):

    return lambda x: a * x + b


line1 = a_line(3, 5)
line2 = a_line(5, 10)
print(line1(10))
print(line1(20))
