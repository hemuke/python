#! /root/anaconda3/bin/python
import time
from multiprocessing import Process
from multiprocessing import current_process


class MyProcess(Process):

    def __init__(self, name, args):
        super().__init__(name=name)
        self.args = args

    def run(self):
        print('子进程启动{}--{}'.format(current_process().pid, current_process().name))
        print('arg1 = {}, arg2 = {}'.format(self.args[0], self.args[1]))
        print('arg1 = %d, arg2 = %d' % (self.args))
        print('子进程结束({}--{})'.format(current_process().pid, current_process().name))


if __name__ == "__main__":
    print(
        '启动父进程pid:{}, name:{}'.format(
            current_process().pid,
            current_process().name))
    process = MyProcess(name="hemuke", args=(5, 8))
    process.start()
    process.join()
    time.sleep(5)
    print(
        '结束父进程pid:{}, name:{}'.format(
            current_process().pid,
            current_process().name))
