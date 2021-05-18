# -*- encoding=utf-8 -*-


"""
send函数

    send函数接受外部调用者的赋值
    
"""
# 生成器逻辑
def func(num):
    while True:
        num1 = yield num
        print('recv num = ', num1)

gen = func(10)
# 激活生成器
print(next(gen))
# 
print(gen.send(1))
print(gen.send(2))
print(gen.send(3))
print(gen.send(4))
