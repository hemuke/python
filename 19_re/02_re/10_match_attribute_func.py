#! /root/anaconda3/bin/python
import re

match_obj = re.compile(r'(\d+)-(?P<sec>\d+)').search('025-3456abc', 1, 7)
print(match_obj)		  #<re.Match object; span=(1, 7), match='25-345'>

print(match_obj.string)		  #025-3456abc
print(match_obj.re)               #re.compile('(\\d+)-(?P<sec>\\d+)')
print(match_obj.pos)              #1
print(match_obj.endpos)           #7
print(match_obj.lastindex)        #2
print(match_obj.lastgroup)        #sec

print(match_obj.group(2))         #345     
print(match_obj.group('sec'))     #345
print(match_obj.group())          #25-345
print(match_obj.group(0))         #25-345
print(match_obj.group(1, 'sec'))  #('25', '345')
print(match_obj.group(1, 2))      #('25', '345')

print(match_obj.groups())         #('25', '345')
print(match_obj.groupdict())      #{'sec': '345'}

print(match_obj.start('sec'))     #4
print(match_obj.start())          #1
print(match_obj.end('sec'))       #7
print(match_obj.end())            #7

print(match_obj.span('sec'))      #(4, 7)
