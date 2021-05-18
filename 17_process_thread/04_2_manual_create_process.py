import time
from multiprocessing import Process
from multiprocessing import current_process

print('父进程启动{}--{}'.format(current_process().pid, current_process().name))


class MyProcess(Process):

    def __init__(self, name, a):
        #        super().__init__(name=name, a=a)
        super().__init__(name=name)
        self.a = a
# 不定义self.name 就能打印self.name的原因是在继承Process时候，Process里面已经定义了name

    def run(self):
        print('子进程启动{}--{}'.format(current_process().pid, current_process().name))
        print(self.name)
        print(self.a)
        time.sleep(5)
        print('子进程结束({}--{})'.format(current_process().pid, current_process().name))


mp = MyProcess(name='myprocess', a=5)
mp.start()

time.sleep(5)
print('父进程结束{}--{}'.format(current_process().pid, current_process().name))
