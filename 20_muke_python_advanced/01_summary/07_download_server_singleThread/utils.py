# -*- encoding=utf-8 -*-


import os


def urllist():
    list_file = os.path.join('piclist/baidu.txt')
    #list_file = os.path.join('20_muke_python_advanced/01_summary/07_download_server_singleThread/scheduler.py')
    #list_file = 'piclist/baidu.txt'
    url_list = []
    with open(list_file, 'r') as f:
        url_list = [line.strip() for line in f]
    return url_list[:]
