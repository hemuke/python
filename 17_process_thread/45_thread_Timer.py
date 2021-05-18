"""
from threading import Timer


def do_sth():
    print('Hello Timer')


timer = Timer(2, do_sth)
timer.start()
"""

from threading import Timer
import time


def do_sth():
    print('Hello Timer')
    global timer
    timer = Timer(3, do_sth)
    timer.start()


timer = Timer(2, do_sth)
timer.start()
time.sleep(15)
print("不加timer.cancel就是死循环")
timer.cancel()
