def func1():
    l = []
    for i in range(10):
        l.append(i)
    return l

for i in func1():
    print(i)

print()

def func2():
    for i in range(10):
        yield i

for i in func2():
    print(i)

for i in func2():
    print(i)
    print('分割线')

print()

def func3():
    yield
    yield from func2()

for i in func3():
    print(i)


t = (i for i in range(2))
for i in t:
     print(i)

for i in t:
     print(i)

# yield把函数变成了生成器
# 生成器代码更加整洁
# yield from允许在一个生成器里迭代另外一个生成器
