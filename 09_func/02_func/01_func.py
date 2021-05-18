#! /root/anaconda3/bin/python
# 例子一
def add(num1, num2):
    return num1 + num2


f = add
print(f(1, 2))

# 例子二
print((lambda num1, num2: num1 + num2)(3, 4))

# 例子三


def le(num1, num2): return num1 + num2


print(le(5, 6))

# 例子四


def eval_enum(x):
    return x * x


print(list(map(eval_enum, [1, 2, 3])))

# 例子五


def do_sth():
    return add


print(do_sth()(7, 8))

# 例子六


def outer():
    def inner():
        print("This is inner.")
    return inner


outer()()
