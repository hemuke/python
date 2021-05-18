#! /root/anaconda3/bin/python
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
#from concurrent.futures import wait
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
# ppe.shutdown(wait=True)
"""
as_completed(fs, timeout=None)
该函数用于将指定的Future实例对象序列转换为一个迭代器，当序列中的任意一个Future实例对象,已经完成或已被取消时都会被yield。这样，通过遍历得到的迭代器，>就可以再任意一个Future实例对象已经完成或已被取消立即做一些处理，比如调用方法result()得到执行结果。
参数fs用于指定Future实例对象序列。
参数timeout用于指定超时时间，如果指定None或不指定，则不会超时。
该函数的返回值是Future实例对象的迭代器。
"""
future_iterator = as_completed(objs)
for future in future_iterator:
    print(future.result())


end = time.time()
print("结束时间{}".format(end - start))
