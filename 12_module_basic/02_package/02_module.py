#! /root/anaconda3/bin/python
"""
from 模块名 import 属性
"""
from os import environ
print(environ)

from os import getenv
print(getenv('PYTHON_HOME'))

from os import MutableMapping
print(MutableMapping)

from xml.dom.minidom import StringTypes
print(StringTypes)

from os import environ, getenv, MutableMapping
print(environ)
print(getenv('PYTHON_HOME'))
print(MutableMapping)

from os import environ as er, getenv as ge , MutableMapping as MM
print(er)
print(ge('PYTHON_HOME'))
print(MM)

from os import *
#强烈不推荐这种导入方式，因为效率低
#代码的可读性差
#容易出错

"""
from 包名 import 模块
"""
from xml.dom import minidom
print(minidom.StringTypes)

