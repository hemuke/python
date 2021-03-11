#! /root/anaconda3/bin/python
import re

print(re.findall(r'\d+', '12=3\n45-6\n78-9\n'))

print(re.findall(r'^\d+', '12=3\n45-6\n78-9\n'))

print(re.findall(r'^\d+', '12=3\n45-6\n78-9\n', re.M))

print(re.findall(r'\A\d+', '12=3\n45-6\n78-9\n'))

print(re.findall(r'\A\d+', '12=3\n45-6\n78-9\n', re.M))

print(re.findall(r'\d+$', '12=3\n45-6\n78-9\n'))

print(re.findall(r'\d+$', '12=3\n45-6\n78-9\n', re.M))

print(re.findall(r'\d+\Z', '12=3\n45-6\n78-9\n', re.M))

print(re.findall(r'\d+\Z', '12=3\n45-6\n78-9', re.M))

print(re.findall(r'\d+\Z', '12=3\n45-6\n78-9'))

print(re.findall(r'\d+\Z', '12=3\n45-6\n78-9\n'))

print(re.match(r'.......', 'a\nb\nc\nd', re.S))

print(re.match(r'.......', 'a\nb\nc\nd'))

print(re.match(r'.......', 'a\nb\nc\nd', re.M))

print(re.findall(r'.......', 'a\nb\nc\nd', re.S))

print(re.findall(r'.......', 'a\nb\nc\nd'))

print(re.findall(r'.......', 'a\nb\nc\nd', re.M))
