#! /root/anaconda3/bin/python
# import 遇到导入模块时候会根据sys模块的modules属性值来查找模块是否已经被导入了

import pprint, sys
pprint.pprint(sys.modules)
print()

# 模块已经被导入了，解释器什么都不做
"""
模块没被导入
  1）解释器按照某种路径搜索模块
  2）[可能]将搜索到的模块编译为Pyc字节码文件
  3）执行编译生成的字节码文件从而运行模块
"""
pprint.pprint(sys.path)
"""
['/opt/python/12_module_basic/10_package',
 '/root/anaconda3/lib/python38.zip',
 '/root/anaconda3/lib/python3.8',
 '/root/anaconda3/lib/python3.8/lib-dynload',
 '/root/anaconda3/lib/python3.8/site-packages']
当前目录
标准库目录
第三方库的安装目录
"""
"""
临时更改模块搜索路径
import sys
sys.path.insert(0, '/tmp/Downloads')
"""
"""
设置环境变量PYTHONPATH永久更改
"""
"""
模块第一次被导入时,__pyache__中的模块会被编译变快
"""
"""
从父包__init__.py 一个个运行
"""
