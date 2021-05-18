#! /root/anaconda3/bin/python
d = {'name': 'Jack'}
print(d.setdefault('name', 'defaultName'))
print(d)

d = {}
print(d.setdefault('name', 'defaultName'))
print(d)

if 'name' not in d:
    d['name'] = 'defaultName'
