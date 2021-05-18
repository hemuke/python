#! /root/anaconda3/bin/python
import time
from threading import Thread
from threading import current_thread

print('父线程%s启动' % current_thread().getName())


class MyThread(Thread):

    def __init__(self, num, name, kwargs):
        super().__init__(name=name)
        self.kwargs = kwargs
        self.num = num

    def run(self):
        print('子线程%s启动' % current_thread().getName())
        time.sleep(5)
        print(self.kwargs)
        print(
            'arg1 = {}, arg2 = {}'.format(
                self.kwargs['arg1'],
                self.kwargs['arg2']))
        print(self.num)
#        print(
#            'arg1 = %d, arg2 = %d' %
#            (self.kwargs['kwargs']['arg1'],
#             self.kwargs['kwargs']['arg2']))
        print('子线程%s结束' % current_thread().getName())


mt = MyThread(10, name='mythread', kwargs={'arg1': 5, 'arg2': 8})
mt.start()

time.sleep(5)
