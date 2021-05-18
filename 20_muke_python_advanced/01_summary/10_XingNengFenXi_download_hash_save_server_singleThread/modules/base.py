# - * - encoding=utf-8 -*-


from const import CalcType

class BaseModule:

    """
    抽象downloader hash模块的公共功能
    """    
    def __init__(self):
        self.calc_type = CalcType.SingleThread

    def set_calc_type(self, type_):
        self.calc_type = type_

    def _process(self, url):
        raise NotImplementedError

    def _process_singlethread(self, list_):
        raise NotImplementedError

    def process(self, list_):
        if self.calc_type == CalcType.SingleThread:
            return self._process_singlethread(list_)
        else:
            pass