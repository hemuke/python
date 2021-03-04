#! /root/anaconda3/bin/python
d = {'name': 'Jack', 'age': 18}
d['age'] = 20
print(d)

d = {'name': 'Jack', 'age': 18}
#d.update(gender = '男', score = 90)
#d.update([('gender', '男'), ('score', 90)])
d.update({'gender': '男', 'score': 90})
print(d)
