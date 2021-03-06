#! /root/anaconda3/bin/python
# 例子一
def outer():
    a = 10

    def inner():
        nonlocal a
        a += 1

        print("例子五，内函数:", a)

    #print("例子五，外函数:", a)
    return inner


# outer()()
#print("例子五__closure__:", outer().__closure__)
#print("例子五__closure__[0].cell_contents:", outer().__closure__[0].cell_contents)

result = outer()
result()
print(result.__closure__[0].cell_contents)
result()
print(result.__closure__[0].cell_contents)
result()
print(result.__closure__[0].cell_contents)

# outer()()
# print(outer().__closure__[0].cell_contents)
# outer()()
# print(outer().__closure__[0].cell_contents)
# outer()()
# print(outer().__closure__[0].cell_contents)
