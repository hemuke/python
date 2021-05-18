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

##########################################################
iterator1 = re.finditer(r'\d+', '-123-56-89-')
for match in iterator1:
    print(match.group())

iterator2 = re.finditer(r'\d+', '-abcd-abcd-abdc-')
for match in iterator2:
    print(match.group())

iterator3 = re.compile(r'\d+').finditer('-123-56-89-')
for match in iterator3:
    print(match.group())

##########################################################
iterator1 = re.finditer(r'-(\d+)-(\d+)-(\d+)-', '-123-56-89-')
for match in iterator1:
    print(match.groups())

iterator2 = re.finditer(r'-(\d+)-(\d+)-(\d+)-', '-abcd-abcd-abdc-')
for match in iterator2:
    print("=====", match.groups())

iterator3 = re.compile(r'-(\d+)-(\d+)-(\d+)-').finditer('-123-56-89-')
for match in iterator3:
    print(match.groups())

##########################################################
iterator1 = re.finditer(r'-(?P<A>\d+)-(?P<B>\d+)-(?P<c>\d+)-', '-123-56-89-')
for match in iterator1:
    print(match.groupdict())

iterator2 = re.finditer(r'-(?P<A>\d+)-(?P<B>\d+)-(?P<c>\d+)-', '-abcd-abcd-abdc-')
for match in iterator2:
    print("=====", match.groupdict())

iterator3 = re.compile(r'-(?P<A>\d+)-(?P<B>\d+)-(?P<c>\d+)-').finditer('-123-56-89-')
for match in iterator3:
    print(match.groupdict())
