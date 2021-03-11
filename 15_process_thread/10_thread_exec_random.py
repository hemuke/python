#! /root/anaconda3/bin/python
from threading import Thread
from threading import current_thread
import time


def do_sth():
    for i in range(5):
        print('%s: %d' % (current_thread().name, i))
        time.sleep(2)


for i in range(3):
    Thread(target=do_sth).start()

do_sth()
