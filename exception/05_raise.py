#! /root/anaconda3/bin/python

#raise ZeroDivisionError('0不能作为除数')
#raise ZeroDivisionError
#raise ZeroDivisionError()

############################################
try:
    raise ZeroDivisionError('0不能作为除数')
except ZeroDivisionError as err:
    print(err)

############################################
try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print(ZeroDivisionError)
############################################
try:
    raise ZeroDivisionError('0不能作为除数')
except ZeroDivisionError:
    raise ValueError('输入错误')
############################################
