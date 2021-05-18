"""
全局变量在多个进程中不能共享
在子进程中修改全局变量，对父进程中的全局变量没影响
子进程对父进程中的全局变量做了一份拷贝，子进程与父进程中的num是完全不同的两个变量
"""

from multiprocessing import Process

num = 18


def do_sth():
    global num
    num += 1
    print(num)


p = Process(target=do_sth)
p.daemon = True
p.start()
p.join()
print(num)
