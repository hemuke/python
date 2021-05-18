#! /root/anaconda3/bin/python
import time
from threading import Thread
from threading import current_thread

print('父线程%s启动' % current_thread().getName())


def do_sth(arg1, arg2):
    print('子线程%s启动' % current_thread().getName())
    time.sleep(30)
    print('arg1 = %d, arg2 = %d' % (arg1, arg2))
    print('子线程%s结束' % current_thread().getName())


thread = Thread(target=do_sth, args=(5, 8))
# thread = Thread(target=do_sth, kwargs={'arg1': 5, 'arg2': 8})
thread.start()

time.sleep(30)
