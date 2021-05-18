##############
# 线程的执行具有随机性和不确定性，添加了cond.wait()和cond.notify()之后，才能使得程序的执行逻辑具有确定性。
#
##############

from multiprocessing import Process, Value, Condition
import time

cond = Condition()
count = Value('i', 0)


class Producer(Process):
    def run(self):
        global count, cond
        while True:
            cond.acquire()
            if count.value < 20:
                count.value += 4
                print('%s：生产者生产了4个，当前总共%d个' % (self.name, count.value))
                # cond.notify()
            else:
                print('%s：不生产，等待' % self.name)
                # cond.wait()
            cond.release()
            time.sleep(2)


class Consumer(Process):
    def run(self):
        global count, cond
        while True:
            cond.acquire()
            if count.value > 10:
                count.value -= 3
                print('%s：消费者消费了3个，当前总共%d个' % (self.name, count.value))
                # cond.notify()
            else:
                print('%s：不消费，等待' % self.name)
                # cond.wait()
            cond.release()
            time.sleep(2)


for i in range(3):
    Producer().start()

for i in range(3):
    Consumer().start()
