#! /root/anaconda3/bin/python
import time
from multiprocessing import Process
from multiprocessing import current_process

print('父进程启动{}--{}'.format(current_process().pid, current_process().name))


class MyProcess(Process):

    def __init__(self, name, args):
        super().__init__(name=name)
        self.args = args

    def run(self):
        print('子进程启动{}--{}'.format(current_process().pid, current_process().name))
        print('arg1 = {}, arg2 = {}'.format(self.args[0], self.args[1]))
        print('arg1 = %d, arg2 = %d' % (self.args))
        time.sleep(20)
        print('子进程结束({}--{})'.format(current_process().pid, current_process().name))


mp = MyProcess(name='myprocess', args=(5, 8))
mp.start()

time.sleep(20)
print('父进程结束{}--{}'.format(current_process().pid, current_process().name))
