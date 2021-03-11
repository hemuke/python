#! /root/anaconda3/bin/python
import re

print(re.match(r'ab*', 'abbbbbbc'))
print(re.match(r'ab*?', 'abbbbbbc'))

print(re.match(r'ab+', 'abbbbbbc'))
print(re.match(r'ab+?', 'abbbbbbc'))

print(re.match(r'ab?', 'abbbbbbc'))
print(re.match(r'ab??', 'abbbbbbc'))

print(re.match(r'ab{3}', 'abbbbbbc'))
print(re.match(r'ab{3}?', 'abbbbbbc'))

print(re.match(r'ab{3,}', 'abbbbbbc'))
print(re.match(r'ab{3,}?', 'abbbbbbc'))

print(re.match(r'ab{3,5}', 'abbbbbbc'))
print(re.match(r'ab{3,5}?', 'abbbbbbc'))
