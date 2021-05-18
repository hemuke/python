#! /root/anaconda3/bin/python
import sys

print(sys.getsizeof(True))  # 28
# 这个True等于数值1
print(sys.getsizeof(False))  # 24
# 这个False等于数值0

print(5 > 3)
print(5 < 3)

print(True == 1)
print(False == 0)
print(True + False + 5)
