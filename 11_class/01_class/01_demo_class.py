#! /root/anaconda3/bin/python
class Dog(object):
    def __init__(self, breed, name, age, health):
        print("2dog实例的内存地址,self", self)
        self.breed = breed
        self.name = name
        self.age = age
        self.health = health

    def run(self):
        print("3dog实例的内存地址,run", self)
        print("Dog is running")

    def bark(self):
        print("4dog实例的内存地址,bark", self)
        print("Dog is barking")

    def bite(self):
        print("5dog实例的内存地址,bite", self)
        print("Dog is biting")


dog = Dog("拉布拉多", "旺财", 3, "很好")
print("1dog实例的内存地址", dog)

# 打印实例属性
print(dog.breed)
print(dog.name)
print(dog.age)
print(dog.health)

dog.run()
dog.bark()
dog.bite()
