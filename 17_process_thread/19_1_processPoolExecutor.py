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


ppe = ProcessPoolExecutor(max_workers=8)

objs = []
for i in range(1, 5):
    future = ppe.submit(do_sth, i)
    objs.append(future)
"""
wait(fs, timeout=None, return_when=ALL_COMPLETED)该函数用于阻塞父进程，以等待指定的Future实例对象序列，直到满足指定的条件。
参数fs用于指定要等待的Future实例对象序列。
参数timeout用于指定等待的最长时间。如果指定为None或不指定，则一直等待
用于return_when用于指定该函数何时返回,有三种取值:FIRST_COMPLETED,FIRST_EXCEPTION,ALL_COMPLETED,分别表示:当第一个Furture实例对象
完成或已被取消时，当第一个Future实例对象抛出异常时，当所有Future实例对象已经完成或以被取消时
"""
# ppe.shutdown(wait=True)
# (done, not_done) = wait(objs, return_when=ALL_COMPLETED)
(done, not_done) = wait(objs, return_when=FIRST_COMPLETED)
print("done:{}".format(done))
print("not_done:{}".format(not_done))

end = time.time()
print("结束时间{}".format(end - start))
