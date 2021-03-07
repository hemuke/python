#! /root/anaconda3/bin/python
import datetime

mot = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

day = datetime.datetime.now().weekday()
print(day)

print(datetime.datetime.now())
print(datetime.datetime.now().weekday())

print(mot[datetime.datetime.now().weekday()])


# 常用函数
L = [1, 2, 3, 4, 4, 4, 4, 4, 4]
print(min(L))
print(max(L))
print(L.count(4))
