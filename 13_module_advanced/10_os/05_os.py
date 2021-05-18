import os

# a/b/c
print(os.path.join("a", "b", "c"))

print(os.path.getatime("/opt/python/13_module_advanced/10_os"))
print(os.path.getatime("/opt/python/13_module_advanced/10_os/README.txt"))


print(os.path.getctime("/opt/python/13_module_advanced/10_os"))
print(os.path.getctime("/opt/python/13_module_advanced/10_os/README.txt"))


print(os.path.getsize("/opt/python/13_module_advanced/10_os"))
print(os.path.getsize("/opt/python/13_module_advanced/10_os/README.txt"))

# 输出操作系统特定的路径分隔符
# linux: /	wn: \\
print(os.sep)


# 输出当前平台使用的行终止符
# linux: \n	win：\r\n
print(os.linesep)

# 输出当前分割文件路径的字符串
# linux: :	win: ;
print(os.pathsep)

# 输出字符串指示当前使用平台
# linux: posix	win: 'nt'
print(os.name)
