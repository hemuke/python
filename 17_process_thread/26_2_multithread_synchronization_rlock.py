from threading import Thread
from threading import RLock
import time

start = time.time()
num = 0

#################################
#为了保证数据的一致性           #
#创建threading属性RLock的实例对象#
#################################
rlock = RLock()


def do_sth():
    global num
    for i in range(1000000):
        """
        # 上锁
        lock.acquire()
        try:
            num += 1
        finally:
        # 解锁
            lock.release()
        """
        with rlock:
            num += 1
        # 由于类对象Lock遵守了上下文管理协议，所以可以使用with语句进行简化。这样，在进入运行时上下文时自动调用方法acquire(),在离开运行时上下文时会自动调用方法release()


t1 = Thread(target=do_sth)
t2 = Thread(target=do_sth)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)
stop = time.time()
print("结束问题{}".format(stop - start))
