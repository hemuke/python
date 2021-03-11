#! /root/anaconda3/bin/python
import time
from multiprocessing import Process
from multiprocessing import current_process

pid = current_process().pid
name = current_process().name

print(f'父进程启动{pid}-{name}')


def do_sth(arg1, arg2):
     print(f'子进程启动{pid}-{name}')
     print(f'arg1 = {arg1}, arg2 = {arg2}')
     print(f'子进程结束{pid}-{name}')


process = Process(target=do_sth, args=(5, 8))
process.start()
time.sleep(20)
print(f'父进程结束{pid}-{name}')
