#! /root/anaconda3/bin/python
from threadpool import ThreadPool
from threadpool import makeRequests
import time
import random

print('父线程启动')

args_list = []
for i in range(1, 11):
    args_list.append(i)


def do_sth(i):
    print('子线程%d启动' % i)

    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()


tp = ThreadPool(3)

# 创建需要线程池处理的任务
requests = makeRequests(do_sth, args_list)

# 把每个任务都给线程池去处理和管理,会自动关闭父线程
for req in requests:
    tp.putRequest(req)

# 父线程会被阻塞
# 线程池管理的所有子线程执行完之后，父线程再从阻塞地方运行 close() join()
tp.wait()

print('父线程结束')
