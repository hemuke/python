#! /root/anaconda3/bin/python
import re

print(re.match(r'...', 'a\nc'))
print(re.match(r'...', 'ab'))
print(re.match(r'...', 'abc'))
print(re.match(r'...', 'abcdef'))

print(re.match(r'[a-z]{7}', 'aBCdefG', re.I))
print(re.match(r'...[a-z]{7}', 'a\naBCdefGs', re.I | re.S))

print(re.match(re.compile(r'...[a-z]{7}', re.S | re.I), 'a\naBcdefGs'))
