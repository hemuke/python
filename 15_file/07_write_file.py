#! /root/anaconda3/bin/python
file = open('myfile3.txt', 'w')
file.writelines(['123\n', '456\n', '789'])
file.flush()
file.close()
