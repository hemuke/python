#! /root/anaconda3/bin/python
import re

print(re.match(r'123|12', '123'))
print(re.compile(r'123|12').match('123'))

print(re.match(r'abc|12', '12'))
print(re.compile(r'abc|12').match('12'))

print(re.match(r'P(ython|erl)', 'Python'))
print(re.compile(r'P(ython|erl)').match('Python'))

print(re.match(r'P(ython|erl)', 'Perl'))
print(re.compile(r'P(ython|erl)').match('Perl'))
