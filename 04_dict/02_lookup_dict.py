#! /root/anaconda3/bin/python
d = {'name': 'Jack', 'age': 18}
print(d['name'])

try:
    print(d['gender'])
except KeyError:
    print(KeyError)

print(d.get('name'))
print(d.get('gender'))
print(d.get('gender', '男'))

print('age' in d)
print('gender' in d)

print('age' not in d)
print('gender' not in d)
