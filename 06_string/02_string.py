#! /root/anaconda3/bin/python
# 修改字符串 原则字符串不能修改的
s = 'Hello,World'
print(s[:5] + '!' + s[6:])

# 字符串比较
print(ord('a'))
print(chr(97))

print(ord('b'))
print(chr(98))

print(ord('A'))
print(chr(65))

print('a' < 'b')
print('a' > 'A')

print('cbadf' > 'cbAeg')

a = b = 'Hello'
c = 'Hello'

print(a == b)
print(a == c)

print(a is b)
print(a is c)
