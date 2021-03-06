#! /root/anaconda3/bin/python
s = '	Hello World	'
print(s.lstrip())
print(s.rstrip())
print(s.strip())

s = 'www.example.com'
print(s.lstrip('comwz.'))
print(s.rstrip('comwz.'))
print(s.strip('comwz.'))
