#! /root/anaconda3/bin/python
try:
    #result = 1 / 2
    result = 1 / 0
except ImportError:
    print("导入错误")
except ZeroDivisionError:
    print("0不能作为除数")
except TypeError:
    print("类型错误")
else:
    print(result)
print("结束")

############################################

# while True:
#    try:
#        x = int(input("请输入一个整数："))
#    except ValueError:
#        print("无效的输入，请再次输入")
#    else:
#        print("输入的整数为：", x)
#        break

while True:
    try:
        x = int(input("请输入一个整数:"))
    except Exception:
        print(Exception)
    else:
        print("输入的整数为：", x)
        break
