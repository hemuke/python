import random
from multiprocessing import Process

import time


class WriteProcess(Process):
    """ 写入文件 """

    def __init__(self, file_name, num, *args, **kwargs):
        # 文件的名称
        self.file_name = file_name
        self.num = num
        super().__init__(*args, **kwargs)

    def run(self):
        """ 写入文件的主要业务逻辑 """
        for i in range(5):
            content = '现在是：{0}：{1} - {2}\n'.format(
                self.name, self.pid, self.num)
            with open(self.file_name, 'a+', encoding='utf-8') as f:
                f.write(content)
                time.sleep(random.randint(1, 5))
                print(content)


if __name__ == '__main__':
    file_name = '49_1_multiprocess_lock.txt'
    for x in range(5):
        p = WriteProcess(file_name, x)
        p.start()
        p.join()
        # 不能写 写了就会每个进程分别写
