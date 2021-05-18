#! /root/anaconda3/bin/python
try:
    result = 1 / 2
    #result = 1 / 0
    #result = int('abc')
except ImportError:
    print("导入错误")
except ZeroDivisionError:
    print("0不能作为除数")
except TypeError:
    print("类型错误")
else:
    print(result)
finally:
    print("释放资源")
print("结束")

############################################
