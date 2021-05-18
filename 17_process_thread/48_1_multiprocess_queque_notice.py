from multiprocessing import Process, Queue, current_process

import random
import time


class WriteProcess(Process):
    """ 写的进程 """

    def __init__(self, q, *args, **kwargs):
        self.q = q
        super().__init__(*args, **kwargs)

    def run(self):
        """ 实现进程的业务逻辑 """
        # 要写的内容
        ls = [
            "第1行内容",
            "第2行内容",
            "第3行内容",
            "第4行内容",
        ]
        for line in ls:
            print('写入内容: {0} - {1}'.format(line, current_process().name))
            self.q.put(line)
            # 每写入一次，休息1-5秒
            # time.sleep(random.randint(1, 5))


class ReadProcess(Process):
    """ 读取内容进程 """

    def __init__(self, q, *args, **kwargs):
        self.q = q
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            content = self.q.get()
            print('读取到的内容：{0} - {1}'.format(content, self.name))


if __name__ == '__main__':
    # 通过Queue共享数据
    print("父进程开始")
    q = Queue()
    # 写入内容的进程
    t_write = WriteProcess(q)
    t_write.start()
    # 读取进程启动
    t_read = ReadProcess(q)
    t_read.start()

    #下面三个参数轮番注释看效果
    t_write.join()
    #t_read.join()

    #由于t_write.join()和t_read.join() 两句代码都注释掉了，读和写进程开启后，就会执行t_read.terminate()代码，把读的进程关闭了，此时只有写的进程在执行，因此结果只显示写的部分不展示读的部分。
    # 因为读的进程是死循环，无法等待其结束，只能强制终止
    t_read.terminate()
    print("父进程结束")
"""
写入内容: 第1行内容 - WriteProcess-1
读取到的内容：第1行内容 - ReadProcess-2
写入内容: 第2行内容 - WriteProcess-1
读取到的内容：第2行内容 - ReadProcess-2
写入内容: 第3行内容 - WriteProcess-1
读取到的内容：第3行内容 - ReadProcess-2
写入内容: 第4行内容 - WriteProcess-1
读取到的内容：第4行内容 - ReadProcess-2
"""
