#! /root/anaconda3/bin/python
s = "Python	Swift	Kotlin"
print(s.split())
print(s.rsplit())

s = "Python|Swift|Kotlin"
print(s.split(sep="|"))
print(s.rsplit(sep="|"))

s = "Python	Swift	Kotlin	Java"
print(s.split(maxsplit=2))
print(s.rsplit(maxsplit=2))

s = "Hello-World-!"
print(s.partition('-'))
print(s.rpartition('-'))

s = "HelloWorld-!"
print(s.partition('-'))
print(s.rpartition('-'))

s = "HelloWorld"
print(s.partition('-'))
print(s.rpartition('-'))

s = '|'.join(['Python', 'Swift', 'Kotlin'])
print(s)

s = ''.join(['Python', 'Swift', 'Kotlin'])
print(s)

s = '|'.join('Python')
print(s)
