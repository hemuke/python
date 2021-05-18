from threading import Thread, Lock, current_thread

numa = 0
numb = 0

locka = Lock()
lockb = Lock()


def do_sth():
    fun1()
    fun2()


def fun1():
    global numa, numb

    locka.acquire()   # 线程1执行这行 第一步

    try:
        print('%s--fun1()--locka' % current_thread().getName())
        numa += 1
        lockb.acquire()   # 线程1执行这行 第三步
        try:
            print('%s--fun1()--lockb' % current_thread().getName())
            numb += 1
        finally:
            lockb.release()
    finally:
        locka.release()


def fun2():
    global numa, numb

    lockb.acquire()  # 线程2执行这个 第二步

    try:
        print('%s--fun2()--lockb' % current_thread().getName())
        numb += 1
        locka.acquire()  # 线程2执行这个 第四步
        try:
            print('%s--fun2()--lockb' % current_thread().getName())
            numa += 1
        finally:
            locka.release()
    finally:
        lockb.release()


tlist = []

for i in range(100):
    t = Thread(target=do_sth)
    tlist.append(t)
    t.start()
#    t.join()

for item in tlist:
    item.join()

print('父线程结束')
