#! /root/anaconda3/bin/python
"""
(base) [root@k8s-ansible ~]# cat /proc/40498/status | grep Threads
Threads:	1
(base) [root@k8s-ansible ~]# cat /proc/40499/status | grep Threads
Threads:	1
看进程的线程
"""
import time
from multiprocessing import Process
from multiprocessing import current_process

print('父进程启动(%d--%s)' % (current_process().pid, current_process().name))


def do_sth(arg1, arg2):
    print('子进程启动(%d--%s)' % (current_process().pid, current_process().name))
    print('arg1 = %d, arg2 = %d' % (arg1, arg2))
    time.sleep(20)
    print('子进程结束(%d--%s)' % (current_process().pid, current_process().name))


if __name__ == "__main__":
    process = Process(target=do_sth, args=(5, 8))
    process.start()
    # process.join()
    time.sleep(10)
    print('父进程结束(%d--%s)' % (current_process().pid, current_process().name))
