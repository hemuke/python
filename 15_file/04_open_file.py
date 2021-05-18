#! /root/anaconda3/bin/python
"""
(base) [root@k8s-ansible file]# cat myfile.txt
1234567890
abcdefghijklmn
opqrstuvwxyz
"""
# readline参数
file = open('myfile.txt')
print(file.readline())
print(file.readline(11))
print(file.readline())
print(file.readline(-5))
file.close()
"""
如果不传参数，读到行尾。
如果传入参数，size用于指定字节数。
    当指定的字节数小于读到行尾的字节数时，读取指定的字节数
    当指定的字节数大于读到行尾的字节数时，或当指定的字节数小于0，读到行尾。
"""
