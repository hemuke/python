from multiprocessing import Process


def do_sth():
    while True:
        pass


Process(target=do_sth).start()
Process(target=do_sth).start()

do_sth()
"""
三个进程占满了八核CPU中的其中三核。因此，多进程可以实现并行(同时处理多个任务)从而发挥多核CPU的最大功效
"""
