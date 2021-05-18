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


tlist = []


for i in range(10):
    t = Thread(target=do_sth)
    tlist.append(t)
    t.start()

for item in tlist:
    item.join()

print(num)
# 这个数值计算错误
