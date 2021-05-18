# -*- encoding=utf-8 -*-


import time
import threading
from concurrent.futures import ThreadPoolExecutor


def _task():
    for i in range(10):
        print('this is a _task. i = {}. thread id = {}'.format(i, threading.get_native_id()))
        time.sleep(1)
    return time.time()


# 初始化最大的数量10个
tp = ThreadPoolExecutor(10)


# # 提交任务 这么写还是串行的
# for _ in range(10):
#     # future对象 获得时候有可能没有完成的
#     future = tp.submit(_task)
#     # 打印每个任务返回的时间
#     print(future.result())

futures = []
for _ in range(2):
    "提交任务"
    future = tp.submit(_task)
    futures.append(future)

for future in futures:
    print(future)
    print(future.result())
