#! /root/anaconda3/bin/python
# https://www.jb51.net/article/120815.htm
# https://www.jb51.net/article/158470.htm
import sys
import ast
x = 7
e = eval('3 * x')
print(e)

d = {'runoob': 'runoob.com', 'google': 'google.com'}
r = repr(d)
print(eval(r))

a = 1
p = {'a': 20}
print(eval('a+1', p))

# 传递全局变量
a = "{'name':'linux','age':age}"
b = eval(a, {"age": 1822})
print(b)
print(type(b))

# 传递本地变量
a = "{'name':'linux','age':age}"
age = 18
b = eval(a, {"age": 1822}, locals())
#b = eval(a,locals())
print(b)
print(type(b))

# 使用eval可以实现从元组，列表，字典型的字符串到元组，列表，字典的转换，此外，eval还可以对字符串型的输入直接计算

create_file = repr(__import__('os').system('echo 123 > /tmp/123.txt'))
open_file = repr(open(r'/tmp/123.txt', 'r').read())
operate_system = repr(__import__('os').system('dir'))
operate_rm = repr(__import__('os').system('rm -f /tmp/123.txt'))

eval(create_file)
eval(open_file)
eval(operate_system)
eval(operate_rm)

# 太危险了需要更改使用as.literal_eval(),只会改用合法的Python类型
try:
    ast.literal_eval('1+1')
except Exception:
    ex_type, ex_value, ex_traceback = sys.exc_info()

    print('异常的类型: %s' % ex_type)
    print('异常的错误信息：%s' % ex_value)
    print('异常调用堆栈的跟踪信息：%s' % ex_traceback)

print(ast.literal_eval('(1,2,3)'))
print(ast.literal_eval('[1,2,3]'))
