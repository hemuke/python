#! /root/anaconda3/bin/python
from threadpool import ThreadPool
from threadpool import makeRequests
import time
import random

print('父线程启动')
#args_list = []
# for i in range(1, 11):
#    args_list.append(i)


def do_sth(i):
    print('子线程%d启动' % i)

    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()

    print('子线程%d结束，耗时%.2f秒' % (i, end - start))


tp = ThreadPool(3)

requests = makeRequests(do_sth, [i for i in range(1, 11)])

for req in requests:
    tp.putRequest(req)

# 父线程被阻塞
# 线程池管理的所有子线程执行完之后，此后会创建并启动由线程池管理的子线程 close() join()
tp.wait()

print('父线程结束')
