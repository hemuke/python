#! /root/anaconda3/bin/python
import copy
"""
    @对于没有嵌套子对象的不可变对象。例如：整数对象、字符串对象、和元组对象等，不会进行拷贝，也就是说，不会创建另一个对象
"""
i1 = 18
i2 = copy.deepcopy(i1)
print(id(i1))                 # 94764035751776
print(id(i2))		      # 94764035751776
print(id(i1) == id(i2))       # true
print()

t1 = (1, 2, 3)
t2 = copy.deepcopy(t1)
print(id(t1))                 # 139899931818944
print(id(t2))                 # 139899931818944
print(id(t1) == id(t2))       # true
print()


"""
    @所谓深拷贝，指的是：对于某个对象，
"""
L1 = [[3, 6], 8]
L2 = copy.deepcopy(L1)
print(id(L1) == id(L2))				# False
print(id(L1[0]) == id(L2[0]))			# False
print(id(L1[0][0]) == id(L2[0][0]))		# True
print(id(L1[0][1]) == id(L2[0][1]))		# True
print(id(L1[1]) == id(L2[1]))			# True
L1[0][0] = 4
print(L1, L2)					# [[4, 6], 8] [[3, 6], 8]
L1[0][1] = 4
print(L1, L2)					# [[4, 4], 8] [[3, 6], 8]
print()


"""
    @如果不可变对象内部又嵌套的子对象，深拷贝之后，会创建一个与该不可变对象具有想通知的另一个对象
"""
t1 = ([3, 6], 8)
t2 = copy.deepcopy(t1)
print(id(t1) == id(t2))				# False
print(id(t1[0]) == id(t2[0]))			# False
print(id(t1[1]) == id(t2[1]))			# True
print(id(t1[0][0]) == id(t2[0][0]))		# True
print(id(t1[0][1]) == id(t2[0][1]))		# True

#t1[1] = 7
#print(t1, t2)

t1[0][0] = 6
print(t1, t2)					# ([6, 6], 8) ([3, 6], 8)
