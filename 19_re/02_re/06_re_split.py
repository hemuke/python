#! /root/anaconda3/bin/python
import re

print(re.split(r'\s+', 'a b 		c d'))
print(re.split(r'\s+', 'a b 		c d', 2))
print(re.split(r'[\s\,\;]+', 'a,  b;; c , ;d	,e;	e'))
print(re.split(r'[\s,;]+', 'a,  b;; c , ;d	,e;	e'))

print(re.compile(r'\s+').split('a b             c d'))
print(re.compile(r'\s+').split('a b             c d', 2))
print(re.compile(r'[\s\,\;]+').split('a,  b;; c , ;d    ,e;     e'))
