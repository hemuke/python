#! /root/anaconda3/bin/python
from threading import current_thread, Thread
import time

print('parent thread: %s start' % (current_thread().getName()))


class MyThread(Thread):

    def run(self):
        print('child thread: %s start' % (current_thread().getName()))
        time.sleep(2)
        print('child thread: %s stop' % (current_thread().getName()))


mt = MyThread()
mt.setDaemon(True)
mt.start()

time.sleep(1)
print('parent thread: %s stop' % (current_thread().getName()))
