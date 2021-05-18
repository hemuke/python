#! /root/anaconda3/bin/python
from multiprocessing import Process
from multiprocessing import current_process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    # p.join()
    print("hello父进程%d结束" % current_process().pid)

"""
main line
module name: __main__
parent process: 60214
process id: 85230
function f
module name: __main__
parent process: 85230
process id: 85231
hello bob
hello父进程85230结束
"""
"""
main line
module name: __main__
parent process: 60214
process id: 85357
hello父进程85357结束
function f
module name: __main__
parent process: 85357
process id: 85358
hello bob
"""
