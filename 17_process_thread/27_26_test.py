import time

start = time.time()


num = 0


def do_sth():
    global num
    for i in range(2000000):
        num += 1


do_sth()
print(num)
stop = time.time()
print("结束问题{}".format(stop - start))

# 因为有GIL lock锁的存在因此单线程还比多线程的速度要快很多。
