# -*- encoding=utf-8 -*-

"""
next函数
    next函数控制执行步骤
”“”
gen = (num for num in range(10))

for i in range(3):
    print(next(gen))   

for i in range(5):
    print(next(gen))   
