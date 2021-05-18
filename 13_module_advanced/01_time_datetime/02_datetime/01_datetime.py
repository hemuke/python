from datetime import datetime
from datetime import date

print(datetime.now())
print(datetime(2021, 1, 2, 12, 40, 22))

t1 = datetime(2021, 3, 22, 13, 40, 30)
t2 = datetime(2021, 3, 22, 14, 50, 11)
print(t2 - t1)
print((t2 - t1).total_seconds())

t = datetime.now()
print(t)
print(t.strftime("%Y年%m月%d日 %H小时%M分钟%S秒"))

#s1 = input('请输入第一个时间(yyyy-MM-dd HH:MM:SS):')
#s2 = input('请输入第二个时间(yyyy-MM-dd HH:MM:SS):')
#
#t1 = datetime.strptime(s1, "%Y-%m-%d %H:%M:%S")
#t2 = datetime.strptime(s2, "%Y-%m-%d %H:%M:%S")
#print(t2 - t1)
