#! /root/anaconda3/bin/python

###########################################################################
# 超级重要
# 同步
# 1)join()方法是主进程会等待子进程结束后再继续运行，即一个进程一个进程的执行
# 2)加锁的意义在于同一时间内只允许一个进程进行操作。当多个进程需要访问共享资源的时候，Lock可以用来避免访问的冲突。例如修改变量的值或多个进程要访问读写同一个文件。
###########################################################################

"""
多进程执行的不确定的性
"""
from multiprocessing import Process
from multiprocessing import current_process
import time
import os


def do_sth():
    for i in range(5):
        print(
            '进程 %s---%d---%d---%d' %
            (current_process().name,
             current_process().pid,
             os.getppid(),
             i))
        time.sleep(1)


# do_sth()

for i in range(3):
    # print('进程cc %s---%d' % (current_process().name, current_process().pid))
    process = Process(target=do_sth)
    process.daemon = True
    process.start()
    # 启动线程
    # process.join()
    print()

do_sth()
"""
print('父进程启动(%d--%s)' % (current_process().pid, current_process().name))


def do_sth(arg1, arg2):
    print('子进程启动(%d--%s)' % (current_process().pid, current_process().name))
    print('arg1 = %d, arg2 = %d' % (arg1, arg2))
    print('子进程结束(%d--%s)' % (current_process().pid, current_process().name))


process = Process(target=do_sth, args=(5, 8))
process.start()
time.sleep(20)
print('父进程结束(%d--%s)' % (current_process().pid, current_process().name))

"""
