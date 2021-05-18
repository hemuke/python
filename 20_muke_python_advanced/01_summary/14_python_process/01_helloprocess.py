# -*- encoding=utf-8 -*-


import multiprocessing
import os
import time


def loop():
    while True:
        print('hello python process.')
        print('process id = {}, parent process id = {}'.format(os.getpid(), os.getppid()))
        time.sleep(1)


cnt = 0


def consumer():
    global cnt
    while True:
        if cnt <= 0:
            time.sleep(1)
            continue
        cnt -= 1
        print('I am a consumer.cnt = {}, process id = {}'.format(cnt, os.getpid()))
        time.sleep(1)


def producer():
    global cnt
    while True:
        cnt += 1
        print('I am a producer, cnt = {}, process id = {}'.format(cnt, os.getpid()))
        time.sleep(10)


if __name__ == '__main__':
    # loop()
    p1 = multiprocessing.Process(target = consumer)
    p2 = multiprocessing.Process(target = producer)
    p1.start()
    p2.start()


# 代码有问题 因为进程不共享变量
# 这个多进程 里面的cnt不是同一个cnt 而是不同线程里面的不同cnt
