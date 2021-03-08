#! /root/anaconda3/bin/python
import re

iterator1 = re.finditer(r'\d+', '-123-56-89-')
for match in iterator1:
    print(match)

iterator2 = re.finditer(r'\d+', '-abcd-abcd-abdc-')
for match in iterator2:
    print(match)

iterator3 = re.compile(r'\d+').finditer('-123-56-89-')
for match in iterator3:
    print(match)
