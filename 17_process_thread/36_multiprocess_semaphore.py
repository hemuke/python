"""
标准库模块threading中提供了一个类对象semaphore，用于表示信号量，它可以帮助我们控制并发线程的最大数量，从而实现多线程之间的同步
"""
"""
信号量里面有一个计数器，一开始是个正整数3, 来一个线程减去1,当这个计数器为0的时候，把要执行的线程放入到信号量等待池，当占用资源的线程释放cond.release()，计数器就加1
"""

from threading import Thread
from threading import Semaphore
import time
import random
sem = Semaphore(10)


class MyThread(Thread):
    def run(self):
        """
        sem.acquire()
        print('%s获得资源' % self.name)
        time.sleep(random.random() * 10)
        sem.release()
        sem.release()
        """
        with sem:
            print('%s获得资源' % self.name)
            #time.sleep(random.random() * 10)
            time.sleep(3)


for i in range(100):
    MyThread().start()
