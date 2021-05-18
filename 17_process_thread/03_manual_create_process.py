#! /root/anaconda3/bin/python
import time
from multiprocessing import Process
from multiprocessing import current_process

print('父进程启动(%d--%s)' % (current_process().pid, current_process().name))


def do_sth(a, b):
    print('子进程启动(%d--%s)' % (current_process().pid, current_process().name))
    time.sleep(20)
    print('a = %d, b = %d' % (a, b))
    print('子进程结束(%d--%s)' % (current_process().pid, current_process().name))


process = Process(target=do_sth, name="hemuke", kwargs={"a": 5, "b": 8})
process.start()
time.sleep(20)
print('父进程结束(%d--%s)' % (current_process().pid, current_process().name))
