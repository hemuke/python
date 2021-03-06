#! /root/anaconda3/bin/python
from string import Template
price = 68.88
book = '<<数据结构与算法>>'

tmpl = Template('花了$p, 买了一本书:$b')
s = tmpl.substitute(p=price, b=book)
print(s)

s = tmpl.substitute({'p': price, 'b': book})
print(s)

s = tmpl.safe_substitute(p=price)
print(s)
