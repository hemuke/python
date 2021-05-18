from threading import Thread
from threading import Lock
from threading import RLock
import time

balance = 0

#################################
#为了保证数据的一致性           #
#创建threading属性Lock的实例对象#
#################################
my_lock = Lock()
your_lock = RLock()


def change_it(n):
    global balance
    try:
        my_lock.acquire()
        balance = balance + n
        print("balance1", balance)
        time.sleep(2)
        balance = balance - n
        print("balance2", balance)
        time.sleep(1)
    finally:
        my_lock.release()


class ChangeBalanceThread(Thread):

    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num

    def run(self):
        for i in range(100):
            change_it(self.num)


if __name__ == '__main__':
    t1 = ChangeBalanceThread(5)
    t2 = ChangeBalanceThread(8)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
