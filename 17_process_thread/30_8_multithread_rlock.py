from threading import Thread
from threading import RLock, Lock

rlock = rLock()

# 标志1
# rlock = Lock()
# 导致死锁的

num = 0


def do_sth():
    global num
    with rlock:
        for i in range(1000000):
            num += 1
    adda()
    addb()
    # 标志1
    # adda()
    # addb()


def adda():
    global num
    with rlock:
        for i in range(1000000):
            num += 1


def addb():
    global num
    with rlock:
        for i in range(1000000):
            num += 1


tlist = []


for i in range(10):
    t = Thread(target=do_sth)
    tlist.append(t)
    t.start()

for item in tlist:
    item.join()

print(num)
# 这个数值计算正确
