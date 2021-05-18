#! /root/anaconda3/bin/python
import re

print(re.findall(r'\bpy\b', 'ab		py cd'))
print(re.findall(r'\bpy\b', 'ab		@py!! cd'))
print(re.findall(r'\bpy\b', 'py as py'))
print(re.findall(r'\bpy\b', 'apy as py'))

print(re.findall(r'\Bpy\w+', 'apy apybc pyb'))
print(re.findall(r'\Bpy\B', 'apyb'))
