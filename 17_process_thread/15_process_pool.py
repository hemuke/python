#! /root/anaconda3/bin/python
from multiprocessing import Pool
import time
import random

print('parent process start')


def do_sth(i):
    print('child process %d start' % (i))

    start = time.time()
    time.sleep(random.random() * 50)
    end = time.time()

    print('child process %d stop, time %.2fs' % (i, end - start))


# pp = pool(8) 不指定默认的是cpu的核数
pp = Pool(3)

for i in range(1, 11):
    # 与方法start()类似，不同的是，创建并启动由进程池管理的子进程
    pp.apply_async(do_sth, args=(i,))

# 调用方法join()之前必须先调用方法close(),否者进程就会被阻塞
# 调用方法close()之后就不能让进程池再管理新的进程了
pp.close()
# 父进程被阻塞
# 进程池管理的所有子进程执行完之后，父进程再从被阻塞的地方继续执行
pp.join()
time.sleep(2)
print('parent process stop')
