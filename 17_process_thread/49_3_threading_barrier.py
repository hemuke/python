# Barrier 栅栏
import threading
import logging
import time
logging.basicConfig(
    level=logging.INFO,
    format="[-] %(threadName)s %(message)s")


def work(barrier: threading.Barrier, i: int):
    logging.info("n_waiting = {}".format(barrier.n_waiting))
    try:
        if i < 3:
            bid = barrier.wait(1)  # 超时1秒就将栅栏置于broken状态，抛出异常后续语句不会执行
        else:
            if i == 6:
                barrier.reset()  # 恢复栅栏
            bid = barrier.wait()
        logging.info("broken status = {}".format(barrier.broken))
        # #是否处于broken状态
        logging.info("after barrier {}".format(bid))
    except threading.BrokenBarrierError:
        logging.info("Broken Barrier in {}".format(threading.current_thread()))


barrier = threading.Barrier(3)

for i in range(1, 12):  # 10个
    threading.Event().wait(0.02)  # 强制延迟2秒,让出时间片
    #time.sleep(0.2)
    threading.Thread(target=work, args=(barrier, i),
                     name="Barrier-{}".format(i)).start()
"""
[-] Barrier-1 n_waiting = 0
[-] Barrier-1 Broken Barrier in <Thread(Barrier-1, started 139726480586496)>
[-] Barrier-2 n_waiting = 0
[-] Barrier-2 Broken Barrier in <Thread(Barrier-2, started 139726480586496)>
[-] Barrier-3 n_waiting = 0
[-] Barrier-3 Broken Barrier in <Thread(Barrier-3, started 139726480586496)>
[-] Barrier-4 n_waiting = 0
[-] Barrier-4 Broken Barrier in <Thread(Barrier-4, started 139726480586496)>
[-] Barrier-5 n_waiting = 0
[-] Barrier-5 Broken Barrier in <Thread(Barrier-5, started 139726480586496)>
[-] Barrier-6 n_waiting = 0
[-] Barrier-7 n_waiting = 1
[-] Barrier-8 n_waiting = 2
[-] Barrier-8 after barrier 2
[-] Barrier-7 after barrier 1
[-] Barrier-6 after barrier 0
[-] Barrier-9 n_waiting = 0
[-] Barrier-10 n_waiting = 1
"""
