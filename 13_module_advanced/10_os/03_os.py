import os

# 运行shell命令，直接显示
os.system("ls /root")

# 运行shell命令，获取执行结果
b = os.popen("ls /root").read() 
o = os.popen("cat /opt/python/13_module_advanced/10_os/README.txt").read()
print(o)
print(b)

# 获取当前工作目录，即当前python脚本工作的目录
print(os.getcwd())

# 切换工作目录，相当于shell下cd
os.chdir("/root")
print(os.getcwd())
