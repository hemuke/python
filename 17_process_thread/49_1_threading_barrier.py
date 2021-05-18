"""
https://www.cnblogs.com/i-honey/p/8076214.html
"""

"""
Barrier实例的方法：
broken  检测栅栏是否处于打破的状态，返回True或False
abort()  将栅栏置于broken状态，等待中的线程或者调用等待方法的线程都会抛出threading.BrokenBarrieError异常，直到reset方法来恢复栅栏
reset()  恢复栅栏，重新开始拦截
"""
import time
import logging
import ng
import threadi
import
logging.basicConfig(
    level=logging.INFO,
    format="[-] %(threadName)s %(message)s")


def work(barrier: threading.Barrier):
    logging.info("n_waiting = {}".format(barrier.n_waiting))
    try:
        bid = barrier.wait()
        logging.info("after barrier {}".format(bid))
    except threading.BrokenBarrierError:
        logging.info("Broken Barrier in {}".format(threading.current_thread()))


barrier = threading.Barrier(3)

for x in range(1, 12):  # 12个
    # time.sleep(0.00001)
    threading.Event().wait(0.000001)
    if x == 3:
        barrier.abort()  # 有一个人坏了规矩
    elif x == 6:
        barrier.reset()
    # threading.Event().wait(0.1)
    a = threading.Thread(target=work, args=(barrier,),
                         name="Barrier-{}".format(x))
    a.start()
    # a.join()
"""
[-] Barrier-1 n_waiting = 0
[-] Barrier-2 n_waiting = 1
[-] Barrier-2 Broken Barrier in <Thread(Barrier-2, started 140135332603648)>
[-] Barrier-1 Broken Barrier in <Thread(Barrier-1, started 140135340996352)>
[-] Barrier-3 n_waiting = 0
[-] Barrier-3 Broken Barrier in <Thread(Barrier-3, started 140135332603648)>
[-] Barrier-4 n_waiting = 0
[-] Barrier-4 Broken Barrier in <Thread(Barrier-4, started 140135332603648)>
[-] Barrier-5 n_waiting = 0
[-] Barrier-6 n_waiting = 1
[-] Barrier-7 n_waiting = 2
[-] Barrier-7 after barrier 2
[-] Barrier-6 after barrier 1
[-] Barrier-5 after barrier 0
[-] Barrier-8 n_waiting = 0
[-] Barrier-9 n_waiting = 1
[-] Barrier-10 n_waiting = 2
[-] Barrier-10 after barrier 2
[-] Barrier-8 after barrier 0
[-] Barrier-9 after barrier 1
[-] Barrier-11 n_waiting = 0
卡住1
"""
"""
[-] Barrier-1 n_waiting = 0
[-] Barrier-2 n_waiting = 1
[-] Barrier-1 Broken Barrier in <Thread(Barrier-1, started 139764024497920)>
[-] Barrier-3 n_waiting = 0
[-] Barrier-3 Broken Barrier in <Thread(Barrier-3, started 139763940062976)>
[-] Barrier-4 n_waiting = 0
[-] Barrier-2 Broken Barrier in <Thread(Barrier-2, started 139764016105216)>
[-] Barrier-5 n_waiting = 0
[-] Barrier-4 Broken Barrier in <Thread(Barrier-4, started 139764024497920)>
[-] Barrier-6 n_waiting = 1
[-] Barrier-7 n_waiting = 2
[-] Barrier-7 after barrier 2
[-] Barrier-6 after barrier 1
[-] Barrier-5 after barrier 0
[-] Barrier-8 n_waiting = 0
[-] Barrier-9 n_waiting = 1
[-] Barrier-10 n_waiting = 2
[-] Barrier-10 after barrier 2
[-] Barrier-8 after barrier 0
[-] Barrier-9 after barrier 1
[-] Barrier-11 n_waiting = 0
卡住2
"""
"""
[-] Barrier-1 n_waiting = 0
[-] Barrier-2 n_waiting = 1
[-] Barrier-1 Broken Barrier in <Thread(Barrier-1, started 140632925714176)>
[-] Barrier-3 n_waiting = 0
[-] Barrier-3 Broken Barrier in <Thread(Barrier-3, started 140632908928768)>
[-] Barrier-2 Broken Barrier in <Thread(Barrier-2, started 140632917321472)>
[-] Barrier-4 n_waiting = 0
[-] Barrier-4 Broken Barrier in <Thread(Barrier-4, started 140632908928768)>
[-] Barrier-5 n_waiting = 0
[-] Barrier-5 Broken Barrier in <Thread(Barrier-5, started 140632908928768)>
[-] Barrier-6 n_waiting = 0
[-] Barrier-7 n_waiting = 1
[-] Barrier-8 n_waiting = 2
[-] Barrier-8 after barrier 2
[-] Barrier-9 n_waiting = 0
[-] Barrier-7 after barrier 1
[-] Barrier-10 n_waiting = 0
[-] Barrier-6 after barrier 0
[-] Barrier-11 n_waiting = 2
[-] Barrier-11 after barrier 2
[-] Barrier-9 after barrier 0
[-] Barrier-10 after barrier 1
正常
"""
"""
[-] Barrier-1 n_waiting = 0
[-] Barrier-2 n_waiting = 1
[-] Barrier-3 n_waiting = 0
[-] Barrier-1 Broken Barrier in <Thread(Barrier-1, started 140334085564160)>
[-] Barrier-2 Broken Barrier in <Thread(Barrier-2, started 140334077171456)>
[-] Barrier-4 n_waiting = 0
[-] Barrier-5 n_waiting = 0
[-] Barrier-6 n_waiting = 0
[-] Barrier-5 after barrier 2
[-] Barrier-4 after barrier 1
[-] Barrier-3 after barrier 0
[-] Barrier-7 n_waiting = 0
[-] Barrier-8 n_waiting = 0
[-] Barrier-8 after barrier 2
[-] Barrier-9 n_waiting = 1
[-] Barrier-7 after barrier 1
[-] Barrier-6 after barrier 0
[-] Barrier-10 n_waiting = 1
[-] Barrier-11 n_waiting = 2
[-] Barrier-11 after barrier 2
[-] Barrier-9 after barrier 0
[-] Barrier-10 after barrier 1
正常
"""
