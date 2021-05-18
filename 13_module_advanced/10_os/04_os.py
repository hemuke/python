import os

# 返回Path规范化的绝对路径
# /opt/python/13_module_advanced/10_os/root
print(os.path.abspath("root"))


# 将Path分割成目录和文件名二元数组返回
# ('', 'root')
print(os.path.split("root"))


# 返回Path目录, 如果是相对目录也是分割./和root
# ('/opt/python/13_module_advanced/10_os', 'root')
print(os.path.split("/opt/python/13_module_advanced/10_os/root"))


# 返回Path目录，其实就是os.path.split(path)的第一个元素
# /opt/python/13_module_advanced/10_os 
print(os.path.dirname("/opt/python/13_module_advanced/10_os/root"))


# 返回path最后的文件名。如果path以/或\结尾，那么返回空值。即os.path.split(path)的第二个元素
# root
print(os.path.basename("/opt/python/13_module_advanced/10_os/root"))


# 如果path存在 True
# False
print(os.path.exists("root"))
# False
print(os.path.exists("/opt/python/13_module_advanced/10_os/root"))
# True
print(os.path.exists("/opt/python/13_module_advanced/10_os"))
# True
print(os.path.exists("./"))


# 如果是绝对路径 True
# False
print(os.path.isabs("root"))
# True
print(os.path.isabs("/opt/python/13_module_advanced/10_os/root"))
# True
print(os.path.isabs("/opt/python/13_module_advanced/10_os"))
# False
print(os.path.isabs("./"))


# 如果是文件 True
# True
print(os.path.isfile("README.txt"))
# True
print(os.path.isfile("/opt/python/13_module_advanced/10_os/README.txt"))
# True
print(os.path.isfile("./README.txt"))


# 如果是绝对路径 True
# False
print(os.path.isdir("root"))
# False
print(os.path.isdir("/opt/python/13_module_advanced/10_os/root"))
# True
print(os.path.isdir("/opt/python/13_module_advanced/10_os"))
# True
print(os.path.isdir("./"))
