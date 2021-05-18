from threading import Thread, Condition
import time

cond = Condition()


class MyThread1(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        cond.acquire()

        print('%s说：1' % self.name)
        cond.notify()
        cond.wait()
        # 调用了cond.wait()这个线程就会被阻塞住

        print('MyThread1 睡眠1秒', time.sleep(1))

        print('%s说：11' % self.name)
        cond.notify()
        cond.wait()

        print('MyThread1 睡眠2秒', time.sleep(2))

        print('%s说：111' % self.name)
        cond.notify()

        cond.release()


class MyThread2(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('MyThread2 睡眠3秒', time.sleep(3))
        cond.acquire()

        print('MyThread2 睡眠4秒', time.sleep(4))
        print('%s说：2' % self.name)
        cond.notify()
        cond.wait()

        print('MyThread2 睡眠5秒', time.sleep(5))
        print('%s说：22' % self.name)
        cond.notify()
        cond.wait()

        print('MyThread2 睡眠6秒', time.sleep(6))
        print('%s说：222' % self.name)

        cond.release()


MyThread1('Thread1').start()
MyThread2('Thread2').start()
# MyThread1('Thread1').start()
