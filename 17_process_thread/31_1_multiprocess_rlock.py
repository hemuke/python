from multiprocessing import Process, Value, RLock
import time

start = time.time()

numa = Value('i', 0)
numb = Value('i', 0)

rlock = RLock()


def do_sth():
    """ """
    """
    rlock.acquire()
    try:
        adda()
        addb()
    finally:
        rlock.release()
    """
    with rlock:
        for i in range(1000000):
            numa.value += 1
        adda()
        addb()


def adda():
    global numa
    """
    rlock.acquire()
    try:
        numa.value += 1
    finally:
        rlock.release()
    """
    with rlock:
        for i in range(1000000):
            numa.value += 1


def addb():
    global numb
    """
    rlock.acquire()
    try:
        numb.value += 1
    finally:
        rlock.release()
    """
    with rlock:
        for i in range(1000000):
            numb.value += 1


plist = []

for i in range(10):
    p = Process(target=do_sth)
    plist.append(p)
    p.start()

for item in plist:
    item.join()

print(numa.value)
print(numb.value)
stop = time.time()
print(stop - start)
