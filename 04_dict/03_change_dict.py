#! /root/anaconda3/bin/python
d = {'name': 'Jack', 'age': 18, 'gender': '男'}
d['age'] = 20
print(d)

d = {'name': 'Jack', 'age': 18, 'gender': '男'}
#d.update(name='Mike', age=20)
#d.update([('name', 'Mike'), ('age', 20)])
d.update({'name': 'Mike', 'age': 20})
print(d)
