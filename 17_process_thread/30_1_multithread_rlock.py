"""多线程同步之RLock"""

"""
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
"""


from threading import RLock
rlock = RLock()

rlock.acquire()
print('获得锁')

rlock.acquire()
print('获得锁')

rlock.acquire()
print('获得锁')

rlock.release()
print('释放锁')

rlock.release()
print('释放锁')

rlock.release()
print('释放锁')
