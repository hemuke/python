from threading import Thread

num = 0


def do_sth():
    global num
    for i in range(1000000):
        # 相当于 num = num + 1
        # 首先计算num + 1，存入临时变量中；然后将临时变量的值赋给
        # cpu调度不正确,因此结果不正确
        num += 1


t1 = Thread(target=do_sth)
t2 = Thread(target=do_sth)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)
"""
多线程调度的不确定性，导致num的结果不确定
"""
