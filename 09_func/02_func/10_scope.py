#! /root/anaconda3/bin/python
# 例子一
print(id(123))
#id = "Global"


def outside():
    #id = "Enclosing"

    def inside():
        #id = "Local"
        print(id)

    inside()


outside()


# 例子二
i = 11


def fun1():
    i = 22
    print(i)


fun1()
print(i)


# 例子三
j = 0


def fun2():
    try:
        print(j)
    except Exception as err:
        print(err)

    j = 5


fun2()
