#! /root/anaconda3/bin/python
from datetime import datetime
book = '<<数据结构与算法>>'

print('买了一本书：{}'.format(book))

price = 68.88

print('花了{}，买了一本书：{}'.format(price, book))

print('花了{0}，买了一本书：{1}，只花了{0}'.format(price, book))

print('花了{p}，买了一本书：{b}，只花了{p}'.format(p=price, b=book))

# 十进制
print('{:d}'.format(58))

# 二进制
print('{:b}'.format(58))

# 十六进制小写
print('{:x}'.format(58))

# 十六进制大写
print('{:X}'.format(58))

# 浮点数
print('{:f}'.format(58))

# 使用逗号作为千位分隔符
print('{:,}'.format(123456789))

print('{0:10}'.format(58))
print('{num:^10}'.format(num=58))

# 总共3位
print('{:.3}'.format(3.1415926))
print('{:.3f}'.format(3.1415926))
print('{:.5}'.format(3.1415926))
print('{:.5}'.format('HelloWorld'))
print('{0:.3}'.format(3.1415926))
print('{num:.3}'.format(num=3.1415926))
print('{:18.3f}'.format(3.1415926))

a = 111111111.22
print('价格是{:,.1f}'.format(a))

# datetime
print('{:%Y-%m-%d %H:%M:%S}'.format(datetime(2018, 8, 18, 18, 18, 18)))

print('{:b}'.format(58))
print(format(58, 'b'))
print('{:8.3f}'.format(3.1415926))
print(format(3.1415926, '8.3f'))
