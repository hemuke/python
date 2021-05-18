#! /root/anaconda3/bin/python
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ALL_COMPLETED
from concurrent.futures import FIRST_COMPLETED
from concurrent.futures import wait
import random
import time
start = time.time()


def do_sth(i):
    time.sleep(random.random() * 10)
    return i * i


with ProcessPoolExecutor(max_workers=8) as ppe:
    objs = []
    for i in range(1, 5):
        # submit返回值是一个Future实例对象，表示子进程锁调用的那个函数的执行(例如: do_sth())。
        # 可以调用Future的方法result()得到这个函数的返回值。result是同步方法直到这个函数do_sth执行完，之后result()结果才会返回，所谓同步是逐个执行。意味着等待，阻塞。这个函数do_sth
        future = ppe.submit(do_sth, i)
        objs.append(future)
"""
wait(fs, timeout=None, return_when=ALL_COMPLETED)该函数用于阻塞父进程，以等待指定的Future实例对象序列，直到满足指定的条件。
参数fs用于指定要等待的Future实例对象序列。
参数timeout用于指定等待的最长时间。如果指定为None或不指定，则一直等待
用于return_when用于指定该函数何时返回,有三种取值:FIRST_COMPLETED,FIRST_EXCEPTION,ALL_COMPLETED,分别表示:当第一个Furture实例对象
完成或已被取消时，当第一个Future实例对象抛出异常时，当所有Future实例对象已经完成或以被取消时
"""

##########################################################################
#因为with上下文管理器包含了shutdown的方法有daemon() close() join()等方法 因此无论FIRST_COMPLETED和ALL_COMPLETED的结果一致#
##########################################################################
#(done, not_done) = wait(objs, return_when=ALL_COMPLETED)
(done, not_done) = wait(objs, return_when=FIRST_COMPLETED)
print("done:{}".format(done))
print("not_done:{}".format(not_done))

end = time.time()
print("结束时间{}".format(end - start))
