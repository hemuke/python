#! /root/anaconda3/bin/python
print('------开始------')
print('第一步')
print('第二步')
print('第三步')
print('------结束------')

#score = 58
# if score >= 60:
#    print("及格了")
# else:
#    print("没及格了")

#score = 61
# if score < 60:
#    print('没过60')
# elif score < 70:
#    print('没过70')
# elif score < 80:
#    print('没过80')
# elif score < 90:
#    print('没过90')
# else:
#    print('过90')

score = 72
if score < 60:
    print('没过60')
else:
    if score < 70:
        print('没过70')
    else:
        if score < 80:
            print('没过80')
        else:
            if score < 90:
                print('没过90')
            else:
                print('过90啦')
