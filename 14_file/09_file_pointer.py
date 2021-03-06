#! /root/anaconda3/bin/python
with open('myfile4.txt', 'r') as file:
    print(file.tell())


with open('myfile4.txt', 'w') as file:
    print(file.tell())


with open('myfile.txt', 'a') as file:
    print(file.tell())

    file.write('hello')
    print(file.tell())

'''
1234567890
abcdefghijklmn
opqrstuvwxyz
hello
world
'''
with open('myfile.txt', 'r') as file:
    print(file.tell())

    print(file.read(3))
    print(file.tell())

    print(file.readline())
    print(file.tell())

    print(file.readline(12))
    print(file.tell())

    print(file.readlines())
    print(file.tell())
