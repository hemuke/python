"""
标准库模块threading中提供了一个类对象semaphore，用于表示信号量，它可以帮助我们控制并发线程的最大数量，从而实现多线程之间的同步
"""
from threading import Thread
from threading import BoundedSemaphore
import time
import random

sem = BoundedSemaphore(3)


class MyThread(Thread):
    def run(self):
        """
        sem.acquire()
        print('%s获得资源' % self.name)
        time.sleep(random.random() * 10)
        sem.release()
        """
        with sem:
            print('%s获得资源' % self.name)
            time.sleep(random.random() * 10)


for i in range(10):
    MyThread().start()
