#! /root/anaconda3/bin/python
from multiprocessing import Process, current_process
import time
import os

def do_sth():
    for i in range(5):
        print('进程 %s---%d---%d---%d' % (current_process().name, current_process().pid, os.getppid(), i))
        time.sleep(1)

for i in range(3):
     # print('进程cc %s---%d' % (current_process().name, current_process().pid))
     process = Process(target=do_sth)
     process.start()
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
