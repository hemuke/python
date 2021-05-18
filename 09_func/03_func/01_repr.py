#! /root/anaconda3/bin/python
# Python3编程出,str() repr()区别
# https://blog.csdn.net/kongsuhongbaby/article/details/87398394

# https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr

# https://blog.csdn.net/qq_43733488/article/details/102635769?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control
import datetime
s = "RUNOOB"
print(repr(s))
# ""RUNOOB""

d = {'runoob': 'runoob.com', 'google': 'google.com'}
print(repr(d))

a = repr(456)
b = str(456)
print(a, b)

a = repr('456')
b = str('456')
print(a, b)

today = datetime.datetime.now()
print(str(today))
# '2012-03-14 09:21:58.130922'
print(repr(today))
# 'datetime.datetime(2012, 3, 14, 9, 21, 58, 130922)'

s = """w'o"w"""
print(repr(s))
# '\'w\\\'o"w\''
print(str(s))
# 'w\'o"w'
# print(eval(str(s))==s)
