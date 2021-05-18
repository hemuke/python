#! /root/anaconda3/bin/python
from concurrent.futures import ProcessPoolExecutor
import time
import random

print('父进程启动')


def do_sth(i):
    print('子进程%d启动' % i)

    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()

    print('子进程%d结束,耗时%.2f秒' % (i, end - start))


# 进程池所能容纳的最大进程数指定为3
ppe = ProcessPoolExecutor(max_workers=3)

for i in range(1, 11):
    # 将需要进程池处理的任务全部交给进程池管理，并负责关闭
    ppe.submit(do_sth, i)

# 将原来的join() close() 功能合并了
ppe.shutdown(wait=True)

print('父进程结束')
