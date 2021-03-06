#! /root/anaconda3/bin/python
for i in range(1, 5):
    if i == 3:
        break
    print("i =", i)

for i in range(1, 5):
    if i == 3:
        continue
    print('i =', i)

for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            break
        print('i =', i, 'j =', j)

for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            continue
        print('i =', i, 'j =', j)
