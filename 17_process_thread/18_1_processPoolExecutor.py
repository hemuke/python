#! /root/anaconda3/bin/python
from concurrent.futures import ProcessPoolExecutor
import time


start = time.time()


def do_sth(i):
    time.sleep(1)
    return i * i


with ProcessPoolExecutor(max_workers=8) as ppe:
    objs = []
    for i in range(1, 10):
        # submit返回值是一个Future实例对象，表示子进程锁调用的那个函数的执行(例如: do_sth())。
        # 可以调用Future的方法result()得到这个函数的返回值。result是同步方法直到这个函数do_sth执行完，之后result()结果才会返回，所谓同步是逐个执行。意味着等待，阻塞。这个函数do_sth
        future = ppe.submit(do_sth, i)
        print(future)
        objs.append(future)

# 改写完就是异步
for obj in objs:
    print(obj.result())

end = time.time()

print("时间{}".format(end - start))
