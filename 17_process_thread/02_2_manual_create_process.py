#! /root/anaconda3/bin/python
import time
from multiprocessing import Process
from multiprocessing import current_process


def do_sth(arg1, arg2):
    print('子进程启动(%d--%s)' % (current_process().pid, current_process().name))
    print('arg1 = %d, arg2 = %d' % (arg1, arg2))
    print('子进程结束(%d--%s)' % (current_process().pid, current_process().name))


if __name__ == "__main__":
    print(
        '启动父进程pid:{}, name:{}'.format(
            current_process().pid,
            current_process().name))
    process = Process(target=do_sth, args=(5, 8))
    process.daemon = True
    process.start()
    process.join()
    time.sleep(5)
    print(
        '结束父进程pid:{}, name:{}'.format(
            current_process().pid,
            current_process().name))
