#! /root/anaconda3/bin/python
s1 = {1, 3, 5, 7, 9}
s2 = {3, 7, 9, 5, 1}

print(s1 == s2)
print(s1 != s2)

##########################################

s1 = {1, 3, 5, 7, 9}
s2 = {2, 3, 6, 7, 10}
s3 = {1, 3, 5, 6, 7, 9}

print(s1.issubset(s2))
print(s1.issubset(s3))

print(s2.issuperset(s1))
print(s3.issuperset(s1))

##########################################
s1 = {1, 3, 5, 7, 9}
s2 = {2, 3, 6, 7, 10}
s3 = {2, 4, 6, 8, 10}

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
