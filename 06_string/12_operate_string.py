#! /root/anaconda3/bin/python
import keyword
print('abc'.isidentifier())
print('123'.isidentifier())

print(keyword.iskeyword('if'))
print(keyword.iskeyword('iF'))

print('\t  \r 	\n'.isspace())

print('abc'.isalpha())
print('abc1'.isalpha())

print('123'.isdecimal())
print('123六VI'.isdecimal())
print('123'.isdecimal())

print('123六VI'.isnumeric())
print('123六VIa'.isnumeric())
print('123'.isnumeric())
