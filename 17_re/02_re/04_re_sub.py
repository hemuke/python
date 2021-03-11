#! /root/anaconda3/bin/python
import re

print(re.sub(r'\d+', '888', '-123-56-89-'))

print(re.sub(r'\d+', '888', '-123-56-89-', 2))
print(re.compile(r'\d+').sub('888', '-123-56-89', 2))
print(re.sub(re.compile(r'\d+'), '888', '-123-56-89', 2))


def add1(match):
    val = match.group()
    num = int(val) + 1
    return str(num)


print(re.sub(r'\d+', add1, '-123-56-89-'))


print(re.sub(r'[aeiou]', '', 'HELLO world', re.I))
