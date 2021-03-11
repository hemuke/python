#! /root/anaconda3/bin/python
import re

match_obj = re.compile(r'(\d+)-(?P<sec>\d+)').search('025-3456abc', 1, 7)
print(match_obj)

print(match_obj.string)
print(match_obj.re)
print(match_obj.pos)
print(match_obj.endpos)
print(match_obj.lastindex)
print(match_obj.lastgroup)

print(match_obj.group(2))
print(match_obj.group('sec'))
print(match_obj.group())
print(match_obj.group(0))
print(match_obj.group(1, 'sec'))

print(match_obj.groups())
print(match_obj.groupdict())

print(match_obj.start('sec'))
print(match_obj.start())
print(match_obj.end('sec'))
print(match_obj.end())

print(match_obj.span('sec'))
