from threading import Thread, Condition
import time

cond = Condition()
count = 0


class Producer(Thread):
    def run(self):
        global count, cond
        while True:
            cond.acquire()
            if count < 20:
                count += 4
                print('%s：生产者生产了4个，当前总共%d个' % (self.name, count))
                cond.notify()
            else:
                print('%s：不生产，等待' % self.name)
                cond.wait()
            print("四十大盗")
            cond.release()
            time.sleep(2)


class Consumer(Thread):
    def run(self):
        global count, cond
        while True:
            cond.acquire()
            if count > 10:
                count -= 3
                print('%s：消费者消费了3个，当前总共%d个' % (self.name, count))
                cond.notify()
            else:
                print('%s：不消费，等待' % self.name)
                cond.wait()
            print("阿里巴巴")
            cond.release()
            time.sleep(2)


# for i in range(6):
for i in range(3):
    Producer().start()

for i in range(3):
    Consumer().start()

# Producer().start()
# Consumer().start()
