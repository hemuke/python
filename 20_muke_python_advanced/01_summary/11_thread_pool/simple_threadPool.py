# -*- encoding=utf-8 -*-


import time
import threading


class SimpleThreadPool:
    """简化的线程池实现
    """

    def __init__(self, size):
        # 创建线程池的对象
        self.pool = []
        # 创建线程池里面的任务
        self.queue = []
        for _ in range(size):
            self.pool.append(threading.Thread(target=self.process))

    def process(self):
        while True:
            if len(self.queue) == 0:
                time.sleep(1)
                continue
            # 出栈
            task = self.queue.pop()
            task()


    def submit(self, task):
        self.queue.append(task)


    def start(self):
        for thread in self.pool:
            thread.start()


def _task():
    for i in range(2):
        print('this is a _task. i = {}. thread id = {}'.format(i, threading.get_native_id()))
        time.sleep(1)


if __name__ == '__main__':
    pool = SimpleThreadPool(10)
    pool.start()
    for i in range(10):
        # 提交几个任务
        pool.submit(_task)

# 线程并发问题 没有考虑
# 任务处理有参数 没有考虑