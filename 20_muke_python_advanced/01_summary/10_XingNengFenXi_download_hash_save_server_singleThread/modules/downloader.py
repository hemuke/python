# -*- encoding=utf-8 -*-
import requests
from PIL import ImageFile
import numpy as np

from const import CalcType
from modules.base import BaseModule


class Downloader(BaseModule):

    def __init__(self):
        # super().__init__()
        super(Downloader, self).__init__()

    def _process(self, url):
        print('download url: {}'.format(url))
        response = requests.get(url)
        content = response.content
        # 图片转nump数组
        parser = ImageFile.Parser()
        parser.feed(content)
        try:
             img = parser.close()
             img = np.array(img)
        except Exception as err:
             print("自定义error", err)
             return
        return img

    def _process_singlethread(self, list_):
        response_list = []
        for url in list_:
            # 图片下载
            img = self._process(url)
            response_list.append(img)
        return response_list

#    def process(self, list_):
#        if self.calc_type == CalcType.SingleThread:
#            return self._process_singlethread(list_)
#        else:
#            pass
