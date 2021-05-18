#! /root/anaconda3/bin/python
import time
import threading

"""
任何一个进程都回自动创建并启动了一个线程
"""
print('自动创建并启动了父(主)线程:{}'.format(threading.current_thread().getName()))

time.sleep(20)
