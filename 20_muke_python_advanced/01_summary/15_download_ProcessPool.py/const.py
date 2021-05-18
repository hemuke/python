# -*- encoding=utf-8 -*-


from enum import Enum


class CalcType(Enum):
#class CalcType:
    """计算类型
    """
    SingleThread = 0
    MultiThread = 1
    MultiProcess = 2
    PyCoroutine = 3

print(CalcType.SingleThread)