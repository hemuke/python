#! /root/anaconda3/bin/python
words = ['Java', 'Python', 'Kotlin', 'Swift', 'Go']
for word in words[:]:
    if len(word) < 5:
        words.remove(word)

print(words)

s = {2, 3, 1}
for number in s:
    print(number)

for number in sorted(s):
    print(number)

d = {'Fruits': 86, 'Books': 88, 'Videos': 83}
for elem in d:
    print(elem)

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, '->', value)
