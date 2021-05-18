# -*- encoding=utf-8 -*-


"""
send函数

    send函数接受外部调用者的赋值
    延时计算
"""
def calc():
    while True:
        r = yield
        result = 3.14 * r * r
        print(result)


gen = calc()
# 激活生成器 下面2种
next(gen)
# gen.send(None)


gen.send(10)
gen.send(20)
