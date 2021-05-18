def generator(num):
    print("num = ", num)
    outer_num = yield num
    print('recv num1 = ', outer_num)
    #sum = (yield num) + outer_num
    sum = yield num + outer_num
    print('recv num2 = ', sum)


gen = generator(10)
print(gen)
print(next(gen))
print(gen.send(20))
print(gen.send(60))

"""
def generator(num):
    print('num = ', num)
    outer_num = yield num
    print('recv num = ', outer_num)
    sum = yield num + outer_num
    print('recv sum = ', sum)
"""
