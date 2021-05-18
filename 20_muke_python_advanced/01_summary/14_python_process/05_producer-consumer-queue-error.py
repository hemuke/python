# -*- encoding=utf-8 -*-


import multiprocessing
import time
import os


def consumer(cnt):
    while True:
        cnt -= 1
        print("I am a consumer. cnt = {}, process id = {}".format(cnt, os.getpid()))
        time.sleep(1)


def producer(cnt):
   
    while True:
        print("I am a producer. cnt = {}, process id = {}".format(cnt, os.getpid()))
        time.sleep(1)
        cnt += 1


if __name__ == '__main__':
    # 父进程
    cnt = 0
    # 子进程1
    p1 = multiprocessing.Process(target=producer, args=(cnt, ))
    # 子进程2
    p2 = multiprocessing.Process(target=consumer, args=(cnt, ))
    p1.start()
    p2.start()

# 这个多进程 里面的cnt不是同一个cnt 而是不同线程里面的不同cnt
