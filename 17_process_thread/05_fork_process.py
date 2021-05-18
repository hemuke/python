#! /root/anaconda3/bin/python
"""
这个不是夸平台的命令
"""
import os
import time

try:
    pid = os.fork()
except OSError:
    print('你的操作系统不支持调用函数fork()')
    exit()

if pid < 0:
    print('复制子进程失败')
elif pid == 0:
    print('我是子进程%d,我的父进程是%d' % (os.getpid(), os.getppid()))
    time.sleep(10)
else:
    print('我是父进程%d,我的子进程是%d' % (os.getpid(), pid))
    time.sleep(10)
