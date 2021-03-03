#! /root/anaconda3/bin/python
"""
    @元组生成式，元组是不可变类型的对象，无法在代码中动态地创建元组对象
    @生成器表达式
"""
ge = (i * i for i in range(1, 7))
print(ge)

print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))
try:
    print(next(ge))
except Exception:
    print(Exception)

ge = (i * i for i in range(1, 7))

for item in ge:
    print(item)
print()
print(item)
