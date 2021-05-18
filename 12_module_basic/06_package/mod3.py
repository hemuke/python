#! /root/anaconda3/bin/python
import a.b.mod3
print(a.b.mod3.m)

from a.b.mod3 import m
print(m)

from a.b import mod3
print(mod3.m)
