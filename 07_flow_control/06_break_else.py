#! /root/anaconda3/bin/python
isBreak = False
n = 0
while n < 5:
    if n == 6:
        isBreak = True
        break
    n += 1
if not isBreak:
    print('循环正常结束，没有执行循环体中的break语句')

n = 0
while n < 4:
    if n == 6:
        break
    n += 1
else:
    print('循环正常结束，没有执行循环体中的break语句')

#############################################################
isBreak = False
for n in range(5):
    if n == 6:
        isBreak = True
        break
if not isBreak:
    print('循环正常结束，没有执行循环体中的break语句')

for n in range(5):
    if n == 6:
        break
else:
    print('循环正常结束，没有执行循环体中的break语句')
