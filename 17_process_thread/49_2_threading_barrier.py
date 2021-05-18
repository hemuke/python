# Barrier 栅栏
import threading
import logging
import time
logging.basicConfig(
    level=logging.INFO,
    format="[-] %(threadName)s %(message)s")

#lock = threading.Lock()


def work(barrier: threading.Barrier, x):
    logging.info("n_waiting = {}".format(barrier.n_waiting))
    if x == 3:
        barrier.abort()  # 有一个人坏了规矩
    elif x == 6:
        barrier.reset()
    try:
        bid = barrier.wait()
        logging.info("after barrier {}".format(bid))
    except threading.BrokenBarrierError:
        logging.info("Broken Barrier in {}".format(threading.current_thread()))


barrier = threading.Barrier(3)

for x in range(1, 12):  # 12个
    threading.Event().wait(0.00001)
    threading.Thread(target=work, args=(barrier, x),
                     name="Barrier-{}".format(x)).start()

"""
[-] Barrier-1 n_waiting = 0
[-] Barrier-2 n_waiting = 1
[-] Barrier-3 n_waiting = 2
[-] Barrier-3 Broken Barrier in <Thread(Barrier-3, started 140519125919488)>
[-] Barrier-2 Broken Barrier in <Thread(Barrier-2, started 140519134312192)>
[-] Barrier-1 Broken Barrier in <Thread(Barrier-1, started 140519142704896)>
[-] Barrier-4 n_waiting = 0
[-] Barrier-4 Broken Barrier in <Thread(Barrier-4, started 140518914782976)>
[-] Barrier-7 n_waiting = 0
[-] Barrier-7 Broken Barrier in <Thread(Barrier-7, started 140519125919488)>
[-] Barrier-5 n_waiting = 0
[-] Barrier-5 Broken Barrier in <Thread(Barrier-5, started 140519142704896)>
[-] Barrier-6 n_waiting = 0
[-] Barrier-8 n_waiting = 0
[-] Barrier-9 n_waiting = 1
[-] Barrier-9 after barrier 2
[-] Barrier-10 n_waiting = 0
[-] Barrier-6 after barrier 0
[-] Barrier-8 after barrier 1
[-] Barrier-11 n_waiting = 1
"""
"""
调度的随机性导致阻塞
"""
