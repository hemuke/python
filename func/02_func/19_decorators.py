#! /root/anaconda3/bin/python
def log(func):
    def wrapper(*args, **kwargs):
        print(func)
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper


@log
def add(sum1, sum2):
    print(sum1, sum2)
    return sum1 + sum2


print(add(1, 2))
