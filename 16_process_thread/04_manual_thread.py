#! /root/anaconda3/bin/python
import time
from threading import Thread
from threading import current_thread


class MyThread(Thread):

    def __init__(self, name, **kwargs):
        super().__init__(name=name)
        self.kwargs = kwargs

    def run(self):
        print('子线程%s启动' % current_thread().getName())
        time.sleep(5)
        print(
            'arg1 = %d, arg2 = %d' %
            (self.kwargs['kwargs']['args1'],
             self.kwargs['kwargs']['args2']))
        print('子线程%s结束' % current_thread().getName())


if __name__ == "__main__":
    print('父线程%s启动' % current_thread().getName())
    process = MyThread(name='mythread', kwargs={"args1": 1, "args2": 2})
    process.start()
    process.join()
    time.sleep(5)
    print('父线程%s启动' % current_thread().getName())
