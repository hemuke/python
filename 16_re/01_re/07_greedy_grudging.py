#! /root/anaconda3/bin/python
import re

print(re.compile(r'ab*').match('abbbbbbc'))
print(re.compile(r'ab*?').match('abbbbbbc'))

print(re.compile(r'ab+').match('abbbbbbc'))
print(re.compile(r'ab+?').match('abbbbbbc'))

print(re.compile(r'ab?').match('abbbbbbc'))
print(re.compile(r'ab??').match('abbbbbbc'))

print(re.compile(r'ab{3}').match('abbbbbbc'))
print(re.compile(r'ab{3}?').match('abbbbbbc'))

print(re.compile(r'ab{3,}').match('abbbbbbc'))
print(re.compile(r'ab{3,}?').match('abbbbbbc'))

print(re.compile(r'ab{3,5}').match('abbbbbbc'))
print(re.compile(r'ab{3,5}?').match('abbbbbbc'))
