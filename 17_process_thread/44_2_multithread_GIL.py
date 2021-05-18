from threading import Thread


def do_sth():
    while True:
        pass


Thread(target=do_sth).start()
Thread(target=do_sth).start()

do_sth()
"""
三个进程占满了八核CPU中的其中一核心。因此，多线程不可以并行，只能并发,交替处理问题.
"""

"""
我们编写的Python代码是通过Python解释器来执行的。通常使用的Python解释器是官方提供的CPython。CPython中有一个GIL（Global Interpreter Lock，全局解释器锁），其作用相当于Lock，任何线程在执行前必须先获得GIL，一个线程在获得GIL后其它线程就不能执行，直到该线程释放GIL。因此，GIL保证了同一时刻只有一个线程可以执行，从而导致Python中的多线程不能实现并行。  PYPY JPYTHON解释器就不会
"""
