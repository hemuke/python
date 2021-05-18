#! /root/anaconda3/bin/python
from multiprocessing import current_process, Process
import time

print('parent process %d start' % (current_process().pid))
print('parent process %d stop' % (current_process().pid))


class MyProcess(Process):

    def run(self):
        print('child process %d start' % current_process().pid)
        print('child process %d stop' % current_process().pid)


mp = MyProcess()
mp.daemon = True
mp.start()
# mp.join()
mp.join(1)
# time.sleep(1)
# time.sleep(3)
#print('parent process %d stop' % (current_process().pid))

# 第一组
# def run(self): time.sleep(2)  time.sleep(1) 里面是休息一秒钟

# 第二组
# 加了mp.join() 就可不用加time.sleep()来保证Python的执行顺序，因为调度顺序CPU不确定
# 在执行子进程的时候,会阻塞父进程
# mp.join(2) 规定进程阻塞的时间
