#! /root/anaconda3/bin/python
import os
"""
os.SEEK_SET
os.SEEK_CUR
os.SEEK_END
"""
"""
1234567890
abcdefghijklmn
opqrstuvwxyz
hello
worldhellohello
"""
with open('myfile.txt', 'rb') as file:
    print(file.tell())

    file.seek(5, os.SEEK_SET)
    print(file.tell())

    file.seek(4, os.SEEK_CUR)
    print(file.tell())

    file.seek(-2, os.SEEK_END)
    print(file.tell())
