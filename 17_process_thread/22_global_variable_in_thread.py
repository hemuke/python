"""
进程内的所有线程共享内存空间，所以，全局变量在进程中的所有线程可以共享
"""

from threading import Thread

num = 18


def do_sth():
    global num
    num += 1
    print(num)


t = Thread(target=do_sth)
t.daemon = True
t.start()
t.join()
print(num)
