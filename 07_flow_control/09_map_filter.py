#! /root/anaconda3/bin/python
result = map(ord, 'abcd')
print(result)
print(list(result))

result = map(str.upper, 'abcd')
print(result)
print(list(result))

result = filter(str.isalpha, '123abc')
print(result)
print(list(result))
