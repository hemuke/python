#! /root/anaconda3/bin/python
s = {3, 4, 5, 6, 7}
s.add(8)
print(s)

# 集合中已存在的元素不会被添加
s.add(8)
print(s)


s = {3, 4, 5, 6, 7}
s.update({2, 8})
s.update([2, 8])
s.update((2, 8))
s.update([(2, 8)])
print(s)
