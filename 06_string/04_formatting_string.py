#! /root/anaconda3/bin/python
# https://www.cnblogs.com/wilber2013/p/4641616.html
from datetime import datetime
print(datetime(2018, 8, 18, 18, 18, 18).strftime('%Y-%m-%d %H:%M:%S'))
print(datetime(2019, 9, 19, 19, 19, 19).strftime('%Y-%m-%d %H:%M:%S'))

book = '<<数据结构与算法>>'
print('买了一本书: %s' % book)

price = 68.88
print('花了%f, 买了一本书: %s' % (price, book))

print('我的工作已经完成了%d%%' % 80)

print('%10d' % 58)
print('%10s' % '58')

print('%.3f' % 3.1415926)
print('%.5s' % 'HelloWorld')

print('%8.3f' % 3.1415926)
