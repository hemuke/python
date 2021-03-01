#! /root/anaconda3/bin/python
# 例子一
def outer():
    a = 10

    def inner():
        print(a)

    return inner


outer()()


# 例子二
def do_sth() -> '测试变量作用域':
    temp = 8
    print(temp)


do_sth()
try:
    print(temp)
except Exception as err:
    print(type(err))
    print(err)


# 例子三
print(outer().__closure__)
print(outer().__closure__[0].cell_contents)
# 第一个外部包的变量
# outer().__clousre__[0].cell_contents
# 第二个外部包的变量
# outer().__clousre__[1].cell_contents
