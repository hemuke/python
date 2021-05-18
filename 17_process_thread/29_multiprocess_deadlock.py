from multiprocessing import Process, Lock, Value, current_process

numa = Value('i', 0)
numb = Value('i', 0)

locka = Lock()
lockb = Lock()


def do_sth():
    fun1()
    fun2()


def fun1():
    global numa, numb

    locka.acquire()  # 进程一 执行的第一步

    try:
        print('%s--fun1()--locka' % current_process().pid)
        numa.value += 1
        lockb.acquire()  # 进程一 执行的第三步
        try:
            print('%s--fun1()--lockb' % current_process().pid)
            numb.value += 1
        finally:
            lockb.release()
    finally:
        locka.release()


def fun2():
    global numa, numb

    lockb.acquire()  # 进程二 执行的第二步

    try:
        print('%s--fun2()--lockb' % current_process().pid)
        numb.value += 1
        locka.acquire()  # 进程二 执行的第四步
        try:
            print('%s--fun2()--lockb' % current_process().pid)
            numa.value += 1
        finally:
            locka.release()
    finally:
        lockb.release()


plist = []

for i in range(100):
    p = Process(target=do_sth)
    plist.append(p)
    p.start()

for item in plist:
    item.join()

print('父进程结束')
