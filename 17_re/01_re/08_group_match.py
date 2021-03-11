#! /root/anaconda3/bin/python
import re

matchobj = re.match(r'(\d+)-(\d+)', '025-3456abc')
matchobj = re.compile(r'(\d+)-(\d+)').match('025-3456abc')
print(matchobj)

print(matchobj.group(1))
print(matchobj.group(2))
print(matchobj.group(0))

matchobj = re.match(r'(?P<fir>\d+)-(?P<sec>\d+)', '025-3456abc')
matchobj = re.compile(r'(?P<fir>\d+)-(?P<sec>\d+)').match('025-3456abc')
print(matchobj.group('fir'))
print(matchobj.group('sec'))
print(matchobj.group(1))
print(matchobj.group(2))
print(matchobj.group(0))

print(re.match(r'(\d+)-(\d+)-(\2)', '025-3456-3456789'))
print(re.compile(r'(\d+)-(\d+)-(\2)').match('025-3456-3456789'))

print(re.match(r'(\d+)-(?P<sec>\d+)-(?P=sec)', '025-3456-3456789'))
print(re.compile(r'(\d+)-(?P<sec>\d+)-(?P=sec)').match('025-3456-3456789'))
