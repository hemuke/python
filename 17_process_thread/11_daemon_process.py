#! /root/anaconda3/bin/python
from multiprocessing import current_process
from multiprocessing import Process
import time

print('parent process: %d start' % (current_process().pid))


class MyProcess(Process):

    def run(self):
        print("child process: %d start" % (current_process().pid))
        time.sleep(2)
        print("child process: %d stop" % (current_process().pid))


mp = MyProcess()
#mp.daemon = False
#mp.daemon = True
mp.start()

# time.sleep(4) #这个命令time.sleep()里面的数字决定不一样的结果
print('parent process: %d stop' % (current_process().pid))

"""
mp.daemon = False
parent process: 125171 start
child process: 125172 start
parent process: 125171 stop
child process: 125172 stop
"""

"""
mp.daemon = True
parent process: 125220 start
child process: 125221 start
parent process: 125220 stop
守护进程是守护父进程的子进程 因此当父进程结束的时候 子进程就没存在必要
"""
