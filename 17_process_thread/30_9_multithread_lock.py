from threading import Thread
from threading import Lock

lock = Lock()

num = 0


def do_sth():
    global num
    try:
        lock.acquire()
        for i in range(1000000):
            num += 1
    finally:
        lock.release()
    adda()
    addb()


def adda():
    global num
    try:
        lock.acquire()
        for i in range(1000000):
            num += 1
    finally:
        lock.release()


def addb():
    global num
    try:
        lock.acquire()
        for i in range(1000000):
            num += 1
    finally:
        lock.release()


tlist = []


for i in range(10):
    t = Thread(target=do_sth)
    tlist.append(t)
    t.start()

for item in tlist:
    item.join()

print(num)
# 计算正确
