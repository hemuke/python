#! /root/anaconda3/bin/python
class Person(object):
    age = 18


p = Person()

print(p.age)

p.age = 19
print(p.age)
print(Person.age)

del p.age
print(p.age)

p1 = Person()
p2 = Person()

p1.age += 2
print(Person.age)
print(p1.age)
print(p2.age)

Person.age += 3
print(Person.age)
print(p1.age)
print(p2.age)
