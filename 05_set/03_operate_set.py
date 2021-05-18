#! /root/anaconda3/bin/python
s1 = {1, 3, 5, 7, 9}
s2 = {2, 3, 6, 7, 10}

print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

s1.intersection_update(s2)
print(s1)
print(s2)
##########################################
s1 = {1, 3, 5, 7, 9}
s2 = {2, 3, 6, 7, 10}

print(s1.union(s2))
print(s1 | s2)
print(s1)
print(s2)
##########################################
s1 = {1, 3, 5, 7, 9}
s2 = {2, 3, 6, 7, 10}

print(s1.difference(s2))
print(s1 - s2)
print(s1)
print(s2)

s1.difference_update(s2)
print(s1)
print(s2)
##########################################
s1 = {1, 3, 5, 7, 9}
s2 = {2, 3, 6, 7, 10}

print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)

s1.symmetric_difference_update(s2)
print(s1)
print(s2)
