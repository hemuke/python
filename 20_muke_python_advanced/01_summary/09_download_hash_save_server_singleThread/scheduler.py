# -*- encoding=utf-8 -*-


import os

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
        # 1.加载图片url列表
        url_list = utils.urllist()
        # 2.调度下载模块
        content_list = self.downloader.process(url_list)
        # 3.调度哈希模块
        md5_list = self.hasher.process(content_list) 
        for md5 in md5_list:
            print(md5)
        # 4.调度存储模块
        item_list = []
        for content, md5 in zip(content_list, md5_list):
            path = self._wrap_path(md5)
            item = (content, path)
            item_list.append(item)
        self.storager.process(item_list)
        
        # item_list = []
        # for content, md5 in zip(content_list, md5_list):
        #     path = self._wrap_path(md5)
        #     item = (content, md5)
        #     item_list.append(item)
        # self.storager.process(item_list)


if __name__ == '__main__':
    Scheduler().process() 