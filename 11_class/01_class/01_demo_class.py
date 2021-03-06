#! /root/anaconda3/bin/python
class Dog(object):
    def __init__(self, breed, name, age, health):
        print("dog实例的内存地址,self", self)
        self.breed = breed
        self.name = name
        self.age = age
        self.health = health

    def run(self):
        print("dog实例的内存地址,run", self)
        print("Dog is running")

    def bark(self):
        print("dog实例的内存地址,bark", self)
        print("Dog is barking")

    def bite(self):
        print("dog实例的内存地址,bite", self)
        print("Dog is biting")


dog = Dog("拉布拉多", "旺财", 3, "很好")
print("dog实例的内存地址", dog)

# 打印类属性
print(dog.breed)
print(dog.name)
print(dog.age)
print(dog.health)

dog.run()
dog.bark()
dog.bite()
