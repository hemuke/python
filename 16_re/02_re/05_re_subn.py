#! /root/anaconda3/bin/python
import re


def add1(match):
    val = match.group()
    num = int(val) + 1
    return str(num)


print(re.subn(r'\d+', add1, '-123-56-89-'))
print(re.compile(r'\d+').subn(add1, '-123-56-789-'))

print(re.subn(r'[aeiou]', '', 'HELLO world', re.I))
print(re.compile(r'[aeiou]').subn('', 'HELLO world', re.I))
