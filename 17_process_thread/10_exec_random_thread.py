#! /root/anaconda3/bin/python
from threading import Thread
from threading import current_thread
import time


def do_sth():
    for i in range(5):
        print('%s: %d' % (current_thread().getName(), i))
        time.sleep(2)


# do_sth()

for i in range(3):
    t = Thread(target=do_sth)
    t.setDaemon(True)
    t.start()
    t.join()

do_sth()
