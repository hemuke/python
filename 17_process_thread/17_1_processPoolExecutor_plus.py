#! /root/anaconda3/bin/python
"""
print('父进程启动')
def do_sth(i):
    print('子进程%d启动' % i)
    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()
    print('子进程%d结束,耗时%.2f秒' % (i, end - start))
ppe = ProcessPoolExecutor(max_workers=3)
for i in range(1, 11):
    ppe.submit(do_sth, i)
ppe.shutdown(wait=True)
print('父进程结束')
"""
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


with ProcessPoolExecutor(max_workers=3) as ppe:
    # 方法一
    #    for i in range(1, 11):
    #        ppe.submit(do_sth, i)
    # 方法二
    ppe.map(do_sth, range(1, 11))

# 将原来的join() close() 功能合并了
# ppe.shutdown(wait=True)

print('父进程结束')
