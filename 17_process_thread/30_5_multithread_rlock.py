from threading import Thread

num = 0


def do_sth():
    global num
    for i in range(1000000):
        num += 1
    adda()
    addb()


def adda():
    global num
    num += 1


def addb():
    global num
    num += 1


for i in range(10):
    t = Thread(target=do_sth)
    t.start()
    t.join()

print(num)
# 这个计算正确
# 原因是t.join()
