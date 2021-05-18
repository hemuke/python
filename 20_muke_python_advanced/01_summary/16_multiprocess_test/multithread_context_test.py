# -*- encoding = utf-8 -*-

"""
测试原理
定义2个进程、2个Queue
p1 p2初始化token
p1 通过Queue1传递 token 到 p2
p2 通过Queue2传递 token 到 p1
"""
import queue
import threading


def test_thread_context_switch():
    """多线程上下文切换成本
    """

    def pass_token1(queue1, queue2):
        for i in range(100000):
            queue2.put(0)
            queue1.get()

    def pass_token2(queue1, queue2):
        for i in range(100000):
            queue1.put(1)
            queue2.get()

    queue1 = queue.Queue()
    queue2 = queue.Queue()
    t1 = threading.Thread(target=pass_token1, args=(queue1, queue2))
    t2 = threading.Thread(target=pass_token2, args=(queue1, queue2))
    t1.start()
    t2.start()


if __name__ == '__main__':
    test_thread_context_switch()
