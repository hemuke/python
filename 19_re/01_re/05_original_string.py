#! /root/anaconda3/bin/python
import re

"""
本来只是字母d，需要用\d进行转义，这个原始字符串r'\d'就能满足,
又因为普通字符串里面\已经被拿来做其他的意义了，要用原来的意义，就要转义回来\\
"""
print(re.match(r'\d', '8'))
print(re.compile(r'\d').match('8'))

print(re.match('\\d', '8'))
print(re.compile('\\d').match('8'))

print(re.match(r'a\\b', 'a\\b'))
print(re.compile(r'a\\b').match('a\\b'))

"""
在普通字符串里面每个\的本意都要用两个\\代替。
"""
print(re.match('a\\\\b', 'a\\b'))
print(re.compile('a\\\\b').match('a\\b'))

print(re.match(r'\[abc\]', '[abc]'))
print(re.match('\[abc\]', '[abc]'))
