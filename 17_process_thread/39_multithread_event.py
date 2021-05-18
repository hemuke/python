from threading import Thread
from threading import Event
from threading import current_thread
import time

event = Event()
print(event.is_set())  # False


def do_sth():
    print('%s开始等待' % current_thread().getName())
    event.wait()
    print('%s等待结束' % current_thread().getName())


for i in range(3):
    Thread(target=do_sth).start()

time.sleep(2)

event.set()

"""
Event实例对象管理者一个内部标志，通过改变这个内部标志的值，可以让一个线程给其他处于阻塞状态的线程发送一个事件信号，从而唤醒这些线程让它们转为运行状态。
1）set(self)
将内部标志设置为True

2）is_set(self)
判断内部标志是否被设置为True

3）clear(self)
将内部标志设置为False

4）wait(self, timeout=None)
当内部标志位false,调用该方法的线程会被阻塞。
直到另外一个线程调用了方法set()将内部标志设置为True，被阻塞的线程才会转为运行状态。
"""
