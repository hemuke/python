#! /root/anaconda3/bin/python
import re

obj = re.compile(r'...')
print(obj)

print(re.match(r'...', 'abcdef'))
print(re.compile(r'...').match('abcdef'))
print(re.compile(r'...').match('abcdef', 1, 3))
print(re.compile(r'..').match('abcdef', 1, 3))

print(re.match(r'...', 'abcdef'))
