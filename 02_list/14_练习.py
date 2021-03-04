#! /root/anaconda3/bin/python
import datetime

mot = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

day = datetime.datetime.now().weekday()
print(day)

print(datetime.datetime.now())
print(datetime.datetime.now().weekday())

print(mot[datetime.datetime.now().weekday()])
