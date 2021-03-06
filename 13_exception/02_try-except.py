#! /root/anaconda3/bin/python

try:
    #result = 1 / 2
    result = 1 / 0
    #result = int('abc')
    print(result)
except ImportError:
    print("导入错误")
except ZeroDivisionError:
    print("0不能作为除数")
except ValueError:
    print("值错误")
except Exception as err:
    print(type(err))
print("结束")

######################################################

try:
    result = 1 / 0
    print(result)
except ArithmeticError:
    print("数学错误")

######################################################

try:
    result = 1 / 0
    print(result)
except ZeroDivisionError:
    print("0不能作为除数")
except ArithmeticError:
    print("数学错误")

try:
    result = 1 / 0
    print(result)
except ArithmeticError:
    print("数学错误")
except ZeroDivisionError:
    print("0不能作为除数")

######################################################

try:
    result = 1 / 0
    print(result)
except TypeError:
    print("运行出错了")
except ZeroDivisionError:
    print("运行出错了")
except ValueError:
    print("运行出错了")

try:
    result = 1 / 0
    print(result)
except (TypeError, ZeroDivisionError, ValueError) as err:
    print(type(err))
    print(err)
# except (TypeError, ZeroDivisionError, ValueError):
#   print(ZeroDivisionError)

######################################################

try:
    result = 1 / 0
    print(result)
except Exception:
    print("其他错误")
