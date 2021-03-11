#! /root/anaconda3/bin/python
import re

print(re.search(r'\d+', '-123-56-89-'))
print(re.search(re.compile(r'\d+'), '-123-56-89'))

print(re.match(r'\d+', '-123-56-89-'))
print(re.compile(r'\d+').match('-123-56-89-'))

print(re.compile(r'\d+').search('-123-56-89'))
print(re.compile(r'\d+').search('-123-56-89', 3, 6))

print(re.compile(r'\d+').search('-ass-56-89'))
print(re.compile(r'\d+').search('-ass-56-89'))
