#! /root/anaconda3/bin/python
"""
(base) [root@k8s-ansible file]# cat myfile.txt
1234567890
abcdefghijklmn
opqrstuvwxyz
"""
# readlines参数
file = open('myfile.txt')
print(file.readlines())
file.close()

# readlines 例子一
file = open('myfile.txt')
print(file.readlines(8))
file.close()

# readlines 例子二
file = open('myfile.txt')
print(file.readlines(15))
file.close()

# readlines 例子三
file = open('myfile.txt')
print(file.readlines(-5))
file.close()

# readlines 例子四
file = open('myfile.txt')
print(file.readlines(29))
file.close()
