#! /root/anaconda3/bin/python
import time
from threading import Thread
from threading import current_thread


class MyThread(Thread):

    def __init__(self, name, args):
        super().__init__(name=name)
        self.args = args

    def run(self):
        print('子线程%s启动' % current_thread().getName())
        time.sleep(20)
        print('arg1 = %d, arg2 = %d' % self.args)
        print('子线程%s结束' % current_thread().getName())


if __name__ == "__main__":
    print('父线程%s启动' % current_thread().getName())
    process = MyThread(name='mythread', kwargs={'arg1': 5, 'arg2': 8})
    process.start()
    process.join()
    time.sleep(5)
    print('父线程%s启动' % current_thread().getName())
