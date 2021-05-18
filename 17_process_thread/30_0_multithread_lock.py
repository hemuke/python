"""多线程同步之Lock"""

from threading import Lock

lock = Lock()

lock.acquire()
print('获得锁')

lock.acquire()
print('获得锁')

lock.release()
print('释放锁')

lock.release()
print('释放锁')
