# -*- encoding=utf-8 -*-
import utils
from modules.downloader import Downloader


class Scheduler:
    """ 调度模块
    """

    def __init__(self):
        self.downloader = Downloader()

    def process(self):
        # 1.加载图片url列表
        # 2.调度下载模块
        url_list = utils.urllist()
        self.downloader.process(url_list)


if __name__ == '__main__':
    Scheduler().process() 
