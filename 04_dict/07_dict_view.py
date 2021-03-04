#! /root/anaconda3/bin/python
d = {'name': 'Jack', 'age': 18}

keys = d.keys()
print(keys)
print(list(keys))

values = d.values()
print(values)
print(list(values))

items = d.items()
print(items)
print(list(items))

d.pop('age')
print(d)

print(keys)
print(values)
print(items)
