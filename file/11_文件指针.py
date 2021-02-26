#! /root/anaconda3/bin/python
import os
"""
0123456789
"""
with open('myfile5.txt', 'r+') as file:
    print(file.tell())

    file.seek(3)
    print(file.tell())

    file.write('Python')
    print(file.tell())
