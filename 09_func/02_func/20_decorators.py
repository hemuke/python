#! /root/anaconda3/bin/python
def log(func):
    def wrapper(*args, **kwargs):
        # print(func)
        print(func.__name__)  # add
        return func(*args, **kwargs)
    return wrapper


@log
# add = log(add)
# add(1, 2) = log(add)(1, 2)
def add(sum1, sum2):
    print(sum1, sum2)
    return sum1 + sum2


print(add(1, 2))
print(add.__name__)  # wrapper
print(log.__name__)  # log
print(log(add).__name__)  # wrapper
print(log(add).__closure__[0])	# <cell at 0x7f3296add3d0: function object at 0x7f328f5d1e50>
print(log(add).__closure__[0].cell_contents)	# <function log.<locals>.wrapper at 0x7f328f5d1e50>
