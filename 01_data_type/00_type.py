#! /root/anaconda3/bin/python
print(type(18))
print(type(5.6))
print(type('Heloo'))

# 网络传输的时候要使用
a: str = "你好!"
b: bytes = a.encode('gbk')
print(b)
c: str = b.decode('gbk')
print(c)
