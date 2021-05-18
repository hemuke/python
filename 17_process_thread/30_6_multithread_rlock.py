from threading import Thread
from threading import RLock

rlock = RLock()

num = 0


def do_sth():
    global num
    with rlock:
        for i in range(1000000):
            num += 1
    adda()
    addb()

# adda()函数也会导致数据不正确，脚本没有导致数据不准确是因为数值太小


def adda():
    global num
#    num += 1
    for i in range(1000000):
        num += 1

# addb()函数也会导致数据不正确，脚本没有导致数据不准确是因为数值太小


def addb():
    global num
#    num += 1
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
