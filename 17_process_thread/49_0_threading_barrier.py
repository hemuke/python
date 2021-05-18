"""
https://www.cnblogs.com/i-honey/p/8076214.html
"""
"""
应用场景：
并发初始化
所有线程都必须初始化完成后，才能继续工作，例如运行前加载数据，检查，如果这些工作没完成就不能正常工作运行。
10个线程做10种工作准备，每个线程负责一种工作，只有10个线程都完成后，才能继续工作，先完成的要等待后完成的线程。
例如，启动一个程序，需要先加载磁盘文件、缓存预热、初始化连接池等工作，这些工作可以齐头并进，不过只有都满足了，程序才能继续向后执行。假设数据库链接失败，则初始化工作失败，就要abort，栅栏broken，所有线程收到异常退出。
工作量
有10个计算任务，完成6个，就算工作完成。
"""
import threading
import logging
logging.basicConfig(
    level=logging.INFO,
    format="[-] %(threadName)s %(message)s")


# def work(barrier: threading.Barrier):
def work(barrier: threading.Barrier):
    logging.info("n_waiting = {}".format(barrier.n_waiting))   # 等待的线程数
    bid = barrier.wait()   # 参与者的id，返回0到线程数减1的数值
    logging.info("after barrier {}".format(bid))  # 栅栏之后


barrier = threading.Barrier(3)  # 3个参与者，每3个开闸放行，0,1,2  4,5,6

for x in range(1, 10):  # 所有参数者个数，4,5,6,10,15
    threading.Event().wait(1)
    threading.Thread(target=work, args=(barrier,),
                     name="Barrier-{}".format(x)).start()

"""
Barrier
栅栏，也叫屏障。可以想象成路障、道闸。
构造方法：
threading.Barrier(parties, action=None, timeout=None)
构建Barrier对象，parties 指定参与方数目，timeout是wait方法未指定时超时的默认值。
n_waiting    当前在栅栏中等待的线程数
parties        通过栅栏所需的线程数
wait(timeout=None) 等待通过栅栏，返回0到线程数-1的整数(barrier_id)，每个线程返回不同。如果wait方法设置了超时，并超时发送，栅栏将处于broken状态。
"""
"""
[-] Barrier-1 n_waiting = 0
[-] Barrier-2 n_waiting = 1
[-] Barrier-3 n_waiting = 2
[-] Barrier-3 after barrier 2
[-] Barrier-2 after barrier 1
[-] Barrier-1 after barrier 0
[-] Barrier-4 n_waiting = 0
[-] Barrier-5 n_waiting = 1
[-] Barrier-6 n_waiting = 2
[-] Barrier-6 after barrier 2
[-] Barrier-5 after barrier 1
[-] Barrier-4 after barrier 0
[-] Barrier-7 n_waiting = 0
[-] Barrier-8 n_waiting = 1
[-] Barrier-9 n_waiting = 2
[-] Barrier-9 after barrier 2
[-] Barrier-8 after barrier 1
[-] Barrier-7 after barrier 0
"""
