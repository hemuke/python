from multiprocessing import Process, Semaphore
import time
import random

sem = Semaphore(3)


class MyProcess(Process):
    def run(self):
        # sem.acquire()
        with sem:
            print('%s获得资源' % self.name)
            time.sleep(random.random() * 10)
        # sem.release()


for i in range(10):
    MyProcess().start()


"""
from multiprocessing import BoundedSemaphore

bsem = BoundedSemaphore(3)
bsem.acquire()
bsem.release()
bsem.release()
调用release()的次数比调用acquire()的次数多，计数器的当前值就会超过它的初始值。为了确保能够及时检测到程序中的这种bug
BoundedSemaphore会报错 Semaphore不会报错
"""
