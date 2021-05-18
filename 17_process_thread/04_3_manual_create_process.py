#! /root/anaconda3/bin/python
import time
from multiprocessing import Process
from multiprocessing import current_process

print('父进程启动{}--{}'.format(current_process().pid, current_process().name))


class MyProcess(Process):

    def __init__(self, name, **kwargs):
        super().__init__(name=name)
        self.kwargs = dict(kwargs)

    def run(self):
        print('子进程启动{}--{}'.format(current_process().pid, current_process().name))
        # print('arg1 = {}, arg2 = {}'.format(self.args[0], self.args[1]))
        # print('arg1 = %d, arg2 = %d' % (self.args))
        print(dict(self.kwargs))
        print(self.kwargs['kwargs']['a'])
        print(self.kwargs['kwargs']['b'])
        time.sleep(20)
        print('子进程结束({}--{})'.format(current_process().pid, current_process().name))


mp = MyProcess(name='myprocess', kwargs={"a": 5, "b": 8})
mp.start()

time.sleep(20)
print('父进程结束{}--{}'.format(current_process().pid, current_process().name))
