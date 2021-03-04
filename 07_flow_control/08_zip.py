#! /root/anaconda3/bin/python
names = ['Jack', 'Mike', 'Tom']
ages = [16, 32, 43]

for i in range(len(names)):
    print(names[i], '的年龄是', ages[i])

print(zip(names, ages))
print(list(zip(names, ages)))

for name, age in list(zip(names, ages)):
    print(name, '的年龄是', age)

for name, age in zip(names, ages):
    print(name, '的年龄是', age)

print(list(zip(range(3), range(5))))

x = [1, 2, 3]
y = [4, 5, 6]

print(list(zip(x, y)))

print(*zip(x, y))
#(1, 4) (2, 5) (3, 6)
print(list(zip(*zip(x, y))))

x2, y2 = zip(*zip(x, y))
print(list(x2))
print(list(y2))
