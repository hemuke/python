#! /root/anaconda3/bin/python
def log(func):
    def wrapper(*args, **kwargs):
        # print(func)
        print(func.__name__) # add
        return func(*args, **kwargs)
    return wrapper


@log  # add = log(add)
def add(sum1, sum2):
    print(sum1, sum2)
    return sum1 + sum2


print(add(1, 2))
print(add.__name__) # wrapper
