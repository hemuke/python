# -*- encoding=utf-8 -*-


import multiprocessing
import time
import os


def consumer(queque):
    while True:
        cnt = queque.get()
        print("I am a consumer. cnt = {}, process id = {}".format(cnt, os.getpid()))
        time.sleep(1)


def producer(queque):
    cnt = 0
    while True:
        queque.put(cnt)
        print("I am a producer. cnt = {}, process id = {}".format(cnt, os.getpid()))
        time.sleep(1)
        cnt += 1


if __name__ == '__main__':
    # 父进程
    queque = multiprocessing.Queue()
    # 子进程1
    p1 = multiprocessing.Process(target=producer, args=(queque, ))
    # 子进程2
    p2 = multiprocessing.Process(target=consumer, args=(queque, ))
    p1.start()
    p2.start()

# 这个多进程 里面的cnt是同一个cnt
