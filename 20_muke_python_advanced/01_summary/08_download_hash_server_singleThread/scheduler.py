# -*- encoding=utf-8 -*-
import utils
from modules.downloader import Downloader
from modules.hasher import Hasher


class Scheduler:
    """ 调度模块
    """

    def __init__(self):
        self.downloader = Downloader()
        self.hasher = Hasher()

    def process(self):
        # 1.加载图片url列表
        url_list = utils.urllist()
        # 2.调度下载模块
        content_list = self.downloader.process(url_list)
        # 3.调度哈希模块
        md5_list = self.hasher.process(content_list) 
        for md5 in md5_list:
            print(md5)


if __name__ == '__main__':
    Scheduler().process() 