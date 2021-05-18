import time
from multiprocessing import Process
from multiprocessing import current_process

print('父进程启动{}--{}'.format(current_process().pid, current_process().name))


class MyProcess(Process):

    def __init__(self, name, **kwargs):
        #        super().__init__(name=name, kwargs={'a': 10, 'b': 8})
        super().__init__(name=name)
        self.kwargs = kwargs

    def run(self):
        print('子进程启动{}--{}'.format(current_process().pid, current_process().name))
        # print('arg1 = {}, arg2 = {}'.format(self.args[0], self.args[1]))
        # print('arg1 = %d, arg2 = %d' % (self.args))
        print(self.name)

        print(self.kwargs['a'])
        print(self.kwargs['b'])
        time.sleep(5)
        print('子进程结束({}--{})'.format(current_process().pid, current_process().name))


#mp = MyProcess(name='myprocess', kwargs={"a": 5, "b": 8})
mp = MyProcess(name='myprocess', a=5, b=8)
#mp = MyProcess(kwargs={"name":'myprocess', "a": 5, "b": 8})
mp.start()

time.sleep(5)
print('父进程结束{}--{}'.format(current_process().pid, current_process().name))
