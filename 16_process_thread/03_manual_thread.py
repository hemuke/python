#! /root/anaconda3/bin/python
import time
from threading import Thread
from threading import current_thread


def do_sth(arg1, arg2):
    print('子线程%s启动' % current_thread().getName())
    time.sleep(5)
    print('arg1 = %d, arg2 = %d' % (arg1, arg2))
    print('子线程%s结束' % current_thread().getName())


if __name__ == "__main__":
    print('父线程%s启动' % current_thread().getName())
    process = Thread(target=do_sth, kwargs={'arg1': 5, 'arg2': 8})
    process.start()
    process.join()
    time.sleep(5)
    print('父线程%s启动' % current_thread().getName())
