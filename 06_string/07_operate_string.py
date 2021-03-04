#! /root/anaconda3/bin/python
s = 'he is learning PYTHON'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())
print()
print(s)

print(s.isupper())
print(s.upper().isupper())

print(s.islower())
print(s.lower().islower())

print(s.istitle())
print(s.title().istitle())

##############################################

print('HelloWorld'.center(18, '*'))
print('HelloWorld'.center(18))
print('HelloWorld'.center(10))

print('HelloWorld'.ljust(18, '*'))
print('HelloWorld'.ljust(18))
print('HelloWorld'.ljust(8))

print('HelloWorld'.rjust(18, '*'))
print('HelloWorld'.rjust(18))
print('HelloWorld'.rjust(8))

##############################################
print('578'. zfill(6))
print('-578'.zfill(10))

print('578'. zfill(3))
print('-578'.zfill(3))
