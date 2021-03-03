#! /root/anaconda3/bin/python
def log(func):
    def wrapper(*args, **kwargs):
        # print(func)
        print(func.__name__) # add
        return func(*args, **kwargs)
    return wrapper


@log  
# add = log(add)
# add(1, 2) = log(add)(1, 2)
def add(sum1, sum2):
    print(sum1, sum2)
    return sum1 + sum2


print(add(1, 2))
print(add.__name__) # wrapper
print(log(add).__name__) # wrapper
print(log(add).__closure__[0])
print(log(add).__closure__[0].cell_contents)
