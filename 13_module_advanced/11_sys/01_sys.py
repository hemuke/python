import sys
# 命令行参数list,第一个元素是程序本身路径
print(sys.argv)

# 获取Python解释程序的版本信息
print(sys.version)

# 返回模块的搜素路径，初始化使用PYTHONPATH环境变量的值
print(sys.path)

# 返回操作系统平台名称
print(sys.platform)

# 退出程序，正常退出时exit(0),错误突出sys.exit(1)
sys.exit(0)
sys.exit(1)
