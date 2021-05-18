"""
进程间通信之共享内存
"""
from multiprocessing import Process
from multiprocessing import Value

num = Value('i', 0)


def do_sth():
    global num
    for i in range(1000000):
        """
        相当于：num.value = num.value + 1
        首先计算 num.value + 1 存入临时变量中
        然后将临时变量的赋值给Num
        """
        num.value += 1


t1 = Process(target=do_sth)
t2 = Process(target=do_sth)

t1.start()
t2.start()

t1.join()
t2.join()

print(num.value)
