#! /root/anaconda3/bin/python
from threading import current_thread, Thread
import time

print('parent thread %s start' % (current_thread().getName()))


class MyThread(Thread):

    def run(self):
        print('child thread %s start' % current_thread().getName())
        time.sleep(5)
        print('child thread %s stop' % current_thread().getName())


mt = MyThread()
mt.daemon = True
# mt.setDaemon(True)
mt.start()
mt.join()
# mp.join(1)
# time.sleep(5)
# 第一次注释 查看进程执行顺序time.sleep(5)
# parent process 75851 start
# parent process 75851 stop
# child process 75852 start
# child process 75852 stop
print('parent thread %s stop' % (current_thread().getName()))
