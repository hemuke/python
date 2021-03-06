#! /root/anaconda3/bin/python
# 字符串的反转
s = '12345'

iterator = reversed(s)
print(iterator)
print(list(iterator))

iterator = reversed(s)
a = list(iterator)
print(''.join(a))

# 字符串的排序
s = 'DBeFac'
print(sorted(s))
print(sorted(s, reverse=True))

print(sorted(s, key=str.lower))

# 列表
L = ['Python', 'Java', 'Swift']
L.sort(key=len)
print(L)

L.sort(key=str.lower)
print(L)
