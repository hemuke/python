#! /root/anaconda3/bin/python
"""
    @如果一个对象同时实现了特殊方法__iter__()和__next__(),那么该对象也被称为迭代器对象，如果该对象用于for-in语句，for-in语句首先会调用特殊方法__iter__()返回一个可迭代对象，然后不断调用该迭代对象的特殊方法__next__()返回了下一次迭代的值，直到遇到StopIteration时退出循环。
"""


class MyIterator(object):
    def __init__(self):
        self.data = 0

    def __iter__(self):
        # 我是self <__main__.MyIterator object at 0x7f037b996610>
        print('我是self', self)
        return self

    def __next__(self):
        if self.data > 5:
            raise StopIteration()
        else:
            self.data += 1
            return self.data


# 我是MyIterator() <__main__.MyIterator object at 0x7f037b996610>
print('我是MyIterator()', MyIterator())
for item in MyIterator():
    print(item)
print(item)
