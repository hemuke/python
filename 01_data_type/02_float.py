#! /root/anaconda3/bin/python
from fractions import Fraction
from decimal import Decimal
import sys

print(sys.getsizeof(123456789.123456789))  # 24
print(sys.getsizeof(12345678919.12345678919))  # 24
print(sys.getsizeof(0.0))  # 24
print(sys.getsizeof(float()))  # 24
print(sys.getsizeof(float(1)))  # 24

print(2.3e8)
print(2.3e-4)

print(1.1 + 2.2 - 3.3)
print(1.1 + 2.2)

print(Decimal('1.1') + Decimal('2.2') - Decimal('3.3'))

print(Fraction(11, 10) + Fraction(22, 10) - Fraction(33, 10))
print(type(Fraction(11, 10) + Fraction(22, 10) - Fraction(33, 10)))
