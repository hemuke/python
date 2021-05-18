# -*- encoding-utf-8 -*-


"""
什么是进程池
    进程池是存放多个进程的容器
    CPU调度进程执行后不会销毁进程
    将进程放回进程池重复利用
    进程是稀缺资源，不应该频繁创建和销毁
    架构解耦，进程创建和业务处理解耦，更加优雅
    进程池是Python使用多进程的最佳实践
"""

"""
进程池标准库ProcessPoolExecutor

task任务 到进程池 
里面有个队列 队列里面有很多的进程 等着处理
"""
import os
from concurrent.futures import ProcessPoolExecutor
import time


pp = ProcessPoolExecutor(5)


def _task():
    for i in range(2):
        print('this is a _task. i = {}, process id = {}'.format(i, os.getpid()))
        time.sleep(1)
    return time.time()


if __name__ == '__main__':
    futures = []
    for i in range(10):
        future = pp.submit(_task)
        futures.append(future)

    for future in futures:
        print(os.getpid(), future.result())
