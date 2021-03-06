#! /root/anaconda3/bin/python
"""
(base) [root@k8s-ansible file]# cat myfile.txt
1234567890
abcdefghijklmn
opqrstuvwxyz
"""
# 例子一查看default_buffer_size的大小
import io
print("IO_DEFAULT_BUFFER_SIZE的大小:", io.DEFAULT_BUFFER_SIZE)
print()
print()

# 打开文件
file = open('myfile.txt')
print("全部读取文件大小:", file.read())
file.close()
print()
print()

# 打开文件
file = open('myfile.txt')
print("第一次读取文件的大小:", file.read(12))
print("第二次读取文件的大小:", file.read(12))
file.close()
print()
print()

# 打开文件
file = open('myfile.txt')
print("第三次读取文件的大小:", file.read(120))
print("第四次读取文件的大小:", file.read(12))
file.close()
print()
print()


# 打开文件
file = open('myfile.txt')
print("第五次读取文件的大小:", file.read(-4))
print("第六次读取文件的大小:", file.read(12))
file.close()
print()
