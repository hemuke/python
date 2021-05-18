"""用于多线程的队列之Queue"""

"""
    为了在多线程中应用队列这种数据结构，标准库模块queue中提供了三个类对象：
（1）Queue
    与模块multiprocessing中的JoinableQueue几乎是相同的，其特点也是"先进先出"。
（2）LifoQueue
    特点是Lifo（Last in first out，后进先出），也就是说，入队和出队都是在队尾。
    后进先出的队列其实就是栈。
（3）PriorityQueue
    队列中的每个对象都有优先级。出队时选择优先级最小的对象。
    
    这三种队列的区别仅仅在于它们出队的顺序。
    
    这三种队列都是多线程安全的，都实现了所有需要的同步机制。
"""
"""线程间通信之队列Queue"""

"""
    如果想要实现线程之间的通信，队列是常见的实现方式之一。
    本节示例使用的队列是Queue。
"""
from threading import Thread, current_thread
from queue import Queue
import time, random

# 写数据的子线程执行的代码
def write(q):
    print('写数据的子线程%s启动' % current_thread().getName())

    for obj in list(range(1, 10)):
        print('写数据：%s' % obj)
        q.put(obj, True)
        time.sleep(random.random() * 3)

    print('写数据：None')
    q.put(None, True)

    # 写数据的子线程被阻塞
    # 所有对象都已经出队并且调用了方法task_done()之后，写数据的子线程再从被阻塞的地方继续执行
    q.join()

    print('写数据的子线程%s结束' % current_thread().getName())

# 读数据的子线程执行的代码
def read(q):
    print('读数据的子线程%s启动' % current_thread().getName())

    while True:
        item = q.get(True)
        if item is None:
            print('读数据：None')
            q.task_done()
            break
        print('读数据：%s' % item)
        time.sleep(random.random() * 3)
        q.task_done()

    print('读数据的子线程%s结束' % current_thread().getName())

print('父线程%s启动' % current_thread().getName())

q = Queue()

tw = Thread(target=write, args=(q,))
tr = Thread(target=read, args=(q,))

tw.start()
tr.start()

tw.join()
tr.join()

print('父线程%s结束' % current_thread().getName())
