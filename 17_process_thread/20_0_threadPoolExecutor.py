#! /root/anaconda3/bin/python
from concurrent.futures import ThreadPoolExecutor
import time
import random

print('父线程启动')


def do_sth(i):
    print('子线程%d启动' % i)

    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()

    print('子线程%d结束，耗时%.2f秒' % (i, end - start))


"""
# 将线程池所能容纳的最大线程数指定为3
tpe = ThreadPoolExecutor(max_workers=3)

# 将需要线程池处理的任务全部交给线程池，此后会创建并启动由线程池管理的子线程
for i in range(1, 11):
    tpe.submit(do_sth, i)

# 父线程被阻塞
# 线程池管理的所有子线程执行完之后，父线程再从被阻塞的地方继续执行
tpe.shutdown(wait=True)
"""
with ThreadPoolExecutor(max_workers=3) as tpe:
    """
    for i in range(1, 11):
        tpe.submit(do_sth, i)
    """
    tpe.map(do_sth, range(1, 11))


print('父线程结束')
# 线程运行后会同时创建3个子线程，第4个子线程需要等前3个子线程执行结束后才会创建开始
