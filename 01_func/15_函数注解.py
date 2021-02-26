#! /root/anaconda3/bin/python
def f(a: 'string type', b: int) -> 'join a with b':
    return a + str(b)


print(f('hello', 12.3))
print(f.__annotations__)
