def func():
    print('hello world')

func()			# hello world

print(type(func))	# <class 'function'> 
                        # hello world
print(type(func()))     # <class 'NoneType'> 


def func2():
    print('hello world')
    yield

func2()			# 空
print(type(func2))      # <class 'function'>
print(type(func2()))	# <class 'generator'>


def func3():
    for i in range(10):
        yield i

func3()
print(type(func3))	# <class 'function'>
print(type(func3()))	# <class 'generator'>

for i in func3():
    print(i)

for i in func3():
    print(i)
