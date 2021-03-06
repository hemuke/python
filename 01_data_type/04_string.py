#! /root/anaconda3/bin/python
import sys

print(sys.getsizeof('A'))  # 50
print(sys.getsizeof('AB'))  # 51
print(sys.getsizeof('ABC'))  # 52
print(sys.getsizeof('测'))  # 76
print(sys.getsizeof('测试'))  # 78
print(sys.getsizeof(' '))  # 50
print(sys.getsizeof(''))  # 49
