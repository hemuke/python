from multiprocessing import Process, Pipe
import os
import time
import random


def send_data(conn):
    print('发送数据的子进程%d启动' % os.getpid())

    print('发送数据：None')
    conn.send(None)

# 发送的数据的进程仍然继续，但是接受数据的进程终止

    for obj in list(range(1, 10)):
        print('发送数据：%s' % obj)
        conn.send(obj)
        time.sleep(random.random() * 3)

#    print('发送数据：None')
#    conn.send(None)

    print('发送数据的子进程%d结束' % os.getpid())


def recv_data(conn):
    print('接收数据的子进程%d启动' % os.getpid())

    while True:
        item = conn.recv()
        if item is None:
            print('接收数据：None')
            break
        print('接收数据：%s' % item)
        time.sleep(random.random() * 3)

    print('接收数据的子进程%d结束' % os.getpid())


print('父进程%d启动' % os.getpid())

cr, cs = Pipe(False)

ps = Process(target=send_data, args=(cs,))
pr = Process(target=recv_data, args=(cr,))

ps.start()
pr.start()

ps.join()
pr.join()

print('父进程%d结束' % os.getpid())

"""
GIL 执行顺序
1）设置 GIL
2）切换进一个线程去运行
3）执行下面操作之一：
    * 指定数量的字节码指令
    * 线程主动让出控制权(可以调用 time.sleep(0)来完成)
4）把线程设置回睡眠状态(切换出线程)
5）解锁GIL
6）重复上面的操作
"""
