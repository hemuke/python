#! /bin/bash
#所有和操作系统相关的内容都在os模块

# 可生成多层递归目录
os.makedirs('dirname1/dirname2')
可生成多层递归目录

# mkdir -p ./dirnames/dirnames1
# 若目录为空，则删除，并递归到上一级目录，如果为空也删除
os.removedirs('dirnames2/dirnames1')

# 生成单级目录，相当于shell中mkdir dirname
# mkdir dirname
os.mkdir('dirname')

# 删除单级空目录，若目录不为空则不能删除
# rmdir dirname
os.rmdir('dirname')

# 列出指定目录下的所有文件和子目录,包括隐藏文件，并以列表方式打印
os.listdir('dirname')

# 删除一个文件
os.remove()

# 重命名
os.rename('oldname', 'newname') 

# 运行shell命令，直接显示
os.system("ls /root")

# 运行shell命令，获取执行结果
os.popen("ls /root").read()
os.popen("cat /opt/python/13_module_advanced/10_os/README.txt").read()

# 获取当前工作目录，即当前python脚本工作的目录
print(os.getcwd())

# 切换工作目录，相当于shell下cd
os.chdir("/root")
print(os.getcwd())

