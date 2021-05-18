#! /root/anaconda3/bin/python
import sys

print(sys.getsizeof(0))  # 24
print(sys.getsizeof(2 ** 0))  # 28
print(sys.getsizeof(2 ** 30))  # 32
print(sys.getsizeof(2 ** 60))  # 36


print(bin(118))
print(oct(118))
print(hex(118))

print(118)
print(0b11110110)
print(0o166)
print(0x76)

print(int(118))
print(int('118'))
print(int(118.2))

print(int('118'))
print(int('1111011', 2))
print(int('0o166', 8))
print(int('0x166', 16))
