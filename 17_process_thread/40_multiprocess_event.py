from threading import Thread
from threading import Event
from threading import current_thread
import time

event = Event()
print(event.is_set())  # False


def do_sth():
    print('%s开始等待' % current_thread().getName())
    event.wait()
    print('%s等待结束' % current_thread().getName())


for i in range(3):
    Thread(target=do_sth).start()

time.sleep(2)

event.set()
