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
