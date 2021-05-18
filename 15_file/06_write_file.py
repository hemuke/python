#! /root/anaconda3/bin/python
file = open('myfile2.txt', 'w')
file.write('hello\n')
file.write('world')
file.flush()
file.close()

file = open('myfile.txt', 'a')
file.write('hello\n')
file.write('world')
file.flush()
file.close()
