# -*- encoding=utf-8 -*-


import os

import prettytable

import utils
from const import CalcType
from modules.downloader import Downloader
from modules.hasher import Hasher
from modules.storager import Storager


class Scheduler:
    """ 调度模块
    """

    def __init__(self):
        self.downloader = Downloader()
        self.hasher = Hasher()
        self.storager = Storager()

    def _wrap_path(self, md5):
        filename = '{}.jpg'.format(md5)
        STORAGE_PATH = os.path.join('.', 'images')
        path = os.path.join(STORAGE_PATH, filename)
        return path

    def process(self):
        time_statictics = {}
        time_statictics['network_time'] = []
        time_statictics['cpu_time'] = []
        time_statictics['disk_time'] = []

        timer = utils.Timer()
        # 1.加载图片url列表
        url_list = utils.urllist()
        # 2.调度下载模块
        timer.tick()
        content_list = self.downloader.process(url_list)
        time_cost = timer.tock()
        time_statictics['network_time'].append(time_cost)
        # 3.调度哈希模块
        timer.tick()
        md5_list = self.hasher.process(content_list) 
        for md5 in md5_list:
            print(md5)
        time_cost = timer.tock()
        time_statictics['cpu_time'].append(time_cost)
        # 4.调度存储模块
        item_list = []
        for content, md5 in zip(content_list, md5_list):
            path = self._wrap_path(md5)
            item = (content, path)
            item_list.append(item)
        timer.tick()
        self.storager.process(item_list)
        time_cost = timer.tock()
        time_statictics['disk_time'].append(time_cost)
        return time_statictics
        # item_list = []
        # for content, md5 in zip(content_list, md5_list):
        #     path = self._wrap_path(md5)
        #     item = (content, md5)
        #     item_list.append(item)
        # self.storager.process(item_list)


    def statictics(self, log):
        table = prettytable.PrettyTable(['类型', '单线程总耗时'])
        network_row = ['network']
        cpu_row = ['cpu']
        disk_row = ['disk']
        network_row.append(log['network_time'][0])
        cpu_row.append(log['cpu_time'][0])
        disk_row.append(log['disk_time'][0])
        table.add_row(network_row)
        table.add_row(cpu_row)
        table.add_row(disk_row)
        print(table)

if __name__ == '__main__':
    scheduler = Scheduler()
    time_statictics = scheduler.process()
    scheduler.statictics(time_statictics)
