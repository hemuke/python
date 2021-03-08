#! /root/anaconda3/bin/python
import re

print(re.findall(r'\d+', '-123-56-89'))
print(re.findall(re.compile(r'\d+'), '-123-56-89'))
print(re.compile(r'\d+').findall('-123-56-89'))

print(re.findall(r'\d+', '-abc-as-sss'))
print(re.findall(re.compile(r'\d+'), '-abc-as-sss'))
print(re.compile(r'\d+').findall('-abc-as-sss'))

print(re.compile(r'\d+').findall('-123-56-89-', 4))

try:
    print(re.findall(re.compile(r'\d+'), '-123-56-89', 4))
except ValueError:
    print(ValueError)

try:
    print(re.findall(re.compile(r'\d+', 4), '-123-56-89'))
except ValueError:
    print(ValueError)
