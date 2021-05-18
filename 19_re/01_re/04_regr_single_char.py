#! /root/anaconda3/bin/python
import re

print(re.match(r'[abc]', 'b'))
print(re.match(r'[abc]', 'a'))
print(re.match(r'[abc]', 'c'))
print(re.match(r'[abc]', 'd'))

print(re.compile(r'[abc]').match('b'))
print(re.compile(r'[abc]').match('a'))
print(re.compile(r'[abc]').match('c'))
print(re.compile(r'[abc]').match('d'))

print(re.match(r'[^abc]', 'f'))
print(re.compile(r'[^abc]').match('f'))

print(re.match(r'[a-zA-Z]', 'M'))
print(re.compile(r'[a-zA-Z]').match('M'))

print(re.match(r'[a-n&h-t]', 'k'))
print(re.compile(r'[a-n&h-t]').match('k'))
