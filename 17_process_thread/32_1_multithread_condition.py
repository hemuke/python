from threading import Thread, Condition
import time

cond = Condition()


class MyThread1(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        # time.sleep(1)
        cond.acquire()

        print('%s说：1' % self.name)
        cond.notify()
        cond.wait()

        time.sleep(1)
        print('%s说：11' % self.name)
        print("MyThread1 cond.notify", cond.notify())
        print("MyThread1 cond.release", cond.release())


class MyThread2(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        # time.sleep(1)
        cond.acquire()

        time.sleep(1)
        print('%s说：2' % self.name)
        cond.notify()
        cond.wait()

        time.sleep(1)
        print('%s说：22' % self.name)
#        cond.notify()

        print("MyThread2 cond.release()", cond.release())


MyThread1('Thread1').start()
MyThread2('Thread2').start()
