#! /root/anaconda3/bin/python
class Dog(object):
    pass


'''
不需要传参的情况
'''
'''
<__main__.Dog object at 0x7f92cf17aa00>
<class '__main__.Dog'>
'''
print(Dog())
print(Dog)
print()

##########################################################


class Cat(object):
    def __init__(self):
        print("self", self)
        self.animal = '猫'


print(Cat().animal)
print()
print(Cat())
