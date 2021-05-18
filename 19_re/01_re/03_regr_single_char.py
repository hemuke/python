#! /root/anaconda3/bin/python
import re

"""
<re.Match object; span=(0, 3), match='c-8'>
<re.Match object; span=(0, 3), match='c-8'>
None
None
"""
print(re.match(r'...', 'c-8'))
print(re.compile(r'...').match('c-8'))

print(re.match(r'...', 'c\n8'))
print(re.compile(r'...').match('c\n8'))

"""
<re.Match object; span=(0, 3), match='c\n8'>
<re.Match object; span=(0, 3), match='c\n8'>
<re.Match object; span=(0, 3), match='123'>
<re.Match object; span=(0, 3), match='123'>
"""
print(re.match(r'...', 'c\n8', re.S))
print(re.compile(r'...', re.S).match('c\n8'))

print(re.match(r'\d\d\d', '123abc'))
print(re.compile(r'\d\d\d').match('123abc'))

"""
None
None
<re.Match object; span=(0, 3), match='a-b'>
<re.Match object; span=(0, 3), match='a_b'>
"""
print(re.match(r'\d\d\d', 'abc123'))
print(re.compile(r'\d\d\d').match('abc123'))

print(re.match(r'\D\D\D', 'a-b123'))
print(re.compile(r'\D\D\D').match('a_b123'))

"""
None
None
<re.Match object; span=(0, 3), match='c_8'>
<re.Match object; span=(0, 3), match='c_8'>
"""
print(re.match(r'\D\D\D', '123a-b'))
print(re.compile(r'\D\D\D').match('123a-b'))

print(re.match(r'\w\w\w', 'c_8###'))
print(re.compile(r'\w\w\w').match('c_8###'))

"""
<re.Match object; span=(0, 3), match='@-#'>
<re.Match object; span=(0, 3), match='@-#'>
"""
print(re.match(r'\W\W\W', '@-#c_8'))
print(re.compile(r'\W\W\W').match('@-#c_8'))

"""
<re.Match object; span=(0, 6), match=' \t\r\n\x0c\x0b'>
<re.Match object; span=(0, 6), match=' \t\r\n\x0c\x0b'>
<re.Match object; span=(0, 6), match=' \t\r\n\x0c\x0b'>
<re.Match object; span=(0, 6), match=' \t\r\n\x0c\x0b'>
"""
print(re.match(r'\s\s\s\s\s\s', ' \t\r\n\f\vabc'))
print(re.compile(r'\s\s\s\s\s\s').match(' \t\r\n\f\vabc'))

print(re.match(r'\s\s\s\s\s\s', ' \t\r\n\f\v'))
print(re.compile(r'\s\s\s\s\s\s').match(' \t\r\n\f\v'))

"""
<re.Match object; span=(0, 3), match='c-3'>
<re.Match object; span=(0, 3), match='c-3'>
<re.Match object; span=(0, 3), match='c-3'>
<re.Match object; span=(0, 3), match='c-3'>
"""
print(re.match(r'\S\S\S', 'c-3 \t'))
print(re.compile(r'\S\S\S').match('c-3 \t'))

print(re.match(r'\S\S\S', 'c-3'))
print(re.compile(r'\S\S\S').match('c-3'))
