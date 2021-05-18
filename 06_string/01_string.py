#! /root/anaconda3/bin/python
# 字符串的定义
print(str('abcd'))
print(str(123))
print(str(12.3))
print(str())

# 字符串打印
print("abc'def'")
print('abc"def"')

print('abc\ndef')
print('abc\rdef')
print('123456\t123\t45')
print('abc\bdef')

# 字符串转义
print('abc\\rdef')
print('arc\'def\'')
print("arc\"def\"")

# 原始字符串
print(r'\tC:\\Promgram Files')
print(R'\tC:\\Promgram Files')

# 语法有错误
# print(r'HelloWorld\')
# print(r'What\'s your name')

# 字符串拼接
print('Hello,' + 'World!')
s = 'Hello' ',' 'World' '!'
print(s)

s = 'Hello' ',' \
    'world' \
    '!'
print(s)

print('Hello' * 3)

# 字符串查找
s = '5739182186'
print(s.index('18'))
print(s.find('18'))
print(s.rindex('18'))
print(s.rfind('18'))

print(s.find('18', 1, 5))
print(s.rfind('18', 1, 5))

try:
    s.index('18', 1, 5)
except Exception:
    print(Exception)

try:
    s.rindex('18', 1, 5)
except Exception:
    print(Exception)
