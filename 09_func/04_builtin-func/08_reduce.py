#! /root/anaconda3/bin/python
from functools import reduce
lst = [1, 2, 3, 4]
print(reduce(lambda x, y: x + y, lst))
print(reduce(lambda x, y: x * y, lst))
print(reduce(lambda x, y: x * y + 1, lst))
print(reduce(lambda x, y: x + y, lst, 5))
"""
-->5+1=6
-->6+2=8
-->8+3=11
-->11+4=15
"""
