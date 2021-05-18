"""
为了某种程度上实现模块内的数据访问控制，可以在模块内定义特殊属性__all__。
这样语句"from 模块名 import *"只能导入特殊属性__all__中定义的属性，但是使用语句"import 模块名"仍然能访问所有属性名
"""

"""
__all__ = ['_v', '_f'. '_C']

_v = 18

def _f():
    pass

def _C(object):
    pass

这个方式__all__的优先级高于_。from modc import * 
print(_f())
print(_v)
"""
