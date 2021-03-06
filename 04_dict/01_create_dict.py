#! /root/anaconda3/bin/python
names = ['张三', '李四', '王五', '赵六']
numbers = ['13333333', '14444444', '15555555', '16666666']
print(numbers[names.index('张三')])

###########################################################

phonebook = {'张三': '13333333',
             '李四': '14444444',
             '王五': '15555555',
             '赵六': '16666666'}
print(phonebook['张三'])

print({'name': 'Jack', 'age': 18})
print({})

print(dict({'name': 'jack', 'age': 18}))
print(dict(name='jack', age=18))
print(dict([('name', 'jack'), ('age', 18)]))
print(dict(zip(range(3), 'ABC')))

print(dict())

###########################################################
print(dict.fromkeys(['name', 'age']))
print(dict.fromkeys(('name', 'age')))
print(dict.fromkeys({'name', 'age'}))

print(dict.fromkeys(('name', 'age'), 'N/A'))
print(dict.fromkeys(['name', 'age'], 'N/A'))
print(dict.fromkeys({'name', 'age'}, 'N/A'))
