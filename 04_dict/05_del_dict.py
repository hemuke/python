#! /root/anaconda3/bin/python
d = {'name': 'Jack', 'age': 18, 'gender': '男'}
print(d.pop('age'))
print(d)

try:
    d.pop('score')
except KeyError:
    print(KeyError)

print(d.pop('score', 90))
d.pop('score', 90)

d = {'name': 'Jack', 'age': 18, 'gender': '男'}
del d['age']
print(d)

d = {'name': 'Jack', 'age': 18, 'gender': '男'}
print(d.popitem())
print(d)

d = {'name': 'Jack', 'age': 18, 'gender': '男'}
d.clear()
print(d)
