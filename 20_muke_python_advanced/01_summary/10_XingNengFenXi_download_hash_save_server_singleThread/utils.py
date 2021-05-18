# -*- encoding=utf-8 -*-


import os
import time

class Timer:
    """
    定义计时器
    """
    def __init__(self):
        self.val = 0


    def tick(self):
        """
        表示计时器的开始
        """
        self.val = time.time()

    def tock(self):
        """
        表示计时器的结束
        """
        return round(time.time() - self.val, 6)
    


def urllist():
    list_file = os.path.join('piclist/baidu.txt')
    #list_file = os.path.join('20_muke_python_advanced/01_summary/07_download_server_singleThread/scheduler.py')
    #list_file = 'piclist/baidu.txt'
    url_list = []
    with open(list_file, 'r') as f:
        url_list = [line.strip() for line in f]
    return url_list[:]