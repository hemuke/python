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


t1 = Thread(target=do_sth)
t2 = Thread(target=do_sth)

t1.start()
t2.start()

t1.join()
t2.join()
print(num)
# 这个计算数值错误
