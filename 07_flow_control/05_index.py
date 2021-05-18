#! /root/anaconda3/bin/python
L = ['Java', 'Python', 'Swift', 'Kotlin']

index = 0
for item in L:
    print('L[{}] = {}'.format(index, item))
    index += 1


for index in range(len(L)):
    print('L[{}] = {}'.format(index, L[index]))

index = 0
while index < len(L):
    print('L[{}] = {}'.format(index, L[index]))
    index += 1

print(enumerate(L))

print(list(enumerate(L)))

print(list(enumerate(L, 1)))

for index, item in list(enumerate(L)):
    print('L[{}] = {}'.format(index, item))

for index, item in enumerate(L):
    print('L[{}] = {}'.format(index, item))
