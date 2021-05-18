# -*- encoding=utf-8 -*-


from PIL import Image

from modules.base import BaseModule


class Storager(BaseModule):
    """
    存储模块
    """

    def _process(self, item):
        content, path = item
        content = Image.fromarray(content.astype('uint8')).convert('RGB')
        content.save(path)

    def _process_singlethread(self, list_):
        # item = (content, path)
        for item in list_:
            self._process(item)