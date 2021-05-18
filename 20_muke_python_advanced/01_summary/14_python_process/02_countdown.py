# -*- encoding = utf-8 -*-


import multiprocessing


cnt = 100000000


def countdown():
    global cnt
    while cnt > 0:
        cnt -= 1


if __name__ == '__main__':
    countdown()

#    p1 = multiprocessing.Process(target = countdown)
#    p2 = multiprocessing.Process(target = countdown)
#    p1.start()
#    p2.start()

# 这个多进程 里面的cnt不是同一个cnt 而是不同线程里面的不同cnt
