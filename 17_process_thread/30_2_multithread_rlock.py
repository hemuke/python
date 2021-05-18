from threading import Thread, RLock, Lock

numa = 0
numb = 0
num = 0
rlock = RLock()
# rlock = Lock() 如果在def adda() def addb()里面就会产生死锁


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
    global num
# 这个还是会导致数据得不到正确的数值，当这个num值很小就不能确定
    for i in range(1000000):
        num += 1
#    num += 1
    with rlock:
        adda()
        addb()
# 上面用


def adda():
    global numa
    """
    rlock.acquire()
    try:
        numa += 1
    finally:
        rlock.release()
    """
    with rlock:
        numa += 1
#    for i in range(1000000):
#        numa += 1


def addb():
    global numb
    """
    rlock.acquire()
    try:
        numb += 1
    finally:
        rlock.release()
    """
    with rlock:
        numb += 1
#    for i in range(1000000):
#        numb += 1


tlist = []

for i in range(10):
    t = Thread(target=do_sth)
    tlist.append(t)
    t.start()

for item in tlist:
    item.join()

print(numa)
print(numb)
print(num)
# 这个计算数值还是可能会错误
