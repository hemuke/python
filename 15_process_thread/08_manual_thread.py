#! /root/anaconda3/bin/python
import time
from threading import Thread
from threading import current_thread

print('父线程%s启动' % current_thread().getName())

class MyThread(Thread):
     
    def __init__(self, name, args):
        super().__init__(name=name)
        self.args = args

    def run(self):
        print('子线程%s启动' % current_thread().getName())
        time.sleep(20)
        print('arg1 = %d, arg2 = %d' % self.args)
        print('子线程%s结束' % current_thread().getName())

#process = Thread(target=do_sth, args=(5, 8))
mt = MyThread(name='mythread', kwargs={'arg1': 5, 'arg2': 8})
mt.start()

time.sleep(25)
