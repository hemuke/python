#! /root/anaconda3/bin/python
import time
from threading import Thread
from threading import current_thread

print('父线程%s启动' % current_thread().getName())


class MyThread(Thread):

    def __init__(self, num, name, args):
        super().__init__(name=name)
        self.args = args
        self.num = num

    def run(self):
        print('子线程%s启动' % current_thread().getName())
        time.sleep(5)
        print(
            'arg1 = %d, arg2 = %d' %
            (self.args[0],
             self.args[1]))
        print(self.num)
        print('子线程%s结束' % current_thread().getName())


mt = MyThread(10, name='mythread', args=(5, 8))
mt.start()

time.sleep(5)
