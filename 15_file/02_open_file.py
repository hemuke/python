#! /root/anaconda3/bin/python
# 例子一
file = open('myfile.txt')
file = open('myfile.txt', 'r')

try:
    file = open('myfile2.txt')
except Exception as err:
    print(err)
    print(type(err))

# 例子二
file = open('myfile.txt', 'w')
file = open('myfile2.txt', 'w')

# 例子三
file = open('myfile.txt', 'a')
file = open('myfile2.txt', 'a')

# 例子四
try:
    file = open('myfile.txt', 'x')
except Exception as err:
    print(type(err))
    print(err)

try:
    file = open('myfile2.txt', 'x')
except Exception as err:
    print(type(err))
    print(err)

# 例子五
file = open('myfile.txt', 'r+')
file = open('myfile2.txt', 'r+')
