#! /root/anaconda3/bin/python
import time
import threading

print('自动创建并启动了父(主)线程:{}'.format(threading.current_thread().getName()))

time.sleep(20)
