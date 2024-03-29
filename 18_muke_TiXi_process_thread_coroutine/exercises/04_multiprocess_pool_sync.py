import random
from multiprocessing import current_process, Pool

import time


def run(file_name, num):
    """
    进程执行的业务逻辑
    往文件中写入数据
    :param file_name: str 文件名称
    :param num: int 写入的数字
    :return: str 写入的结果
    """
    with open(file_name, 'a+', encoding='utf-8') as f:
        # 当前的进程
        now_process = current_process()
        # 写入的内容
        conent = '{0} - {1} - {2}'.format(
            now_process.name,
            now_process.pid,
            num
        )
        f.write(conent)
        f.write('\n')
        # 写完之后随机休息1-5秒
        time.sleep(random.randint(1, 5))
        print(conent)
    return 'ok'


if __name__ == '__main__':
    file_name = '50_0_multiprocess_pool_sync.txt'
    with open(file_name, 'w'):
        pass
    # 进程池
    pool = Pool(2)
    for i in range(20):
        # A组 同步添加任务
        rest = pool.apply(run, args=(file_name, i))
        print('{0}---{1}'.format(i, rest))
    # 关闭池子
    pool.close()
    pool.join()
