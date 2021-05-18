# -*- encoding=utf-8 -*-


import multiprocessing


cnt = 0


def consumer():
    global cnt
    while True:
        cnt -= 1


def producer():
    global cnt
    while True:
        cnt += 1


if __name__ == '__main__':

    p1 = multiprocessing.Process(target=consumer)
    p2 = multiprocessing.Process(target=producer)
    p1.start()
    p2.start()

# 这个多进程 里面的cnt不是同一个cnt 而是不同线程里面的不同cnt
