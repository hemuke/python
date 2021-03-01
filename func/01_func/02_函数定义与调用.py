#! /root/anaconda3/bin/python


def decide_args(arg1, arg2):
    if arg1 and arg2:
        return arg1, arg2
    elif (not arg1) and (not arg2):
        return
    else:
        # result = arg1 or arg2
        return arg1 or arg2


print(decide_args)
print(type(decide_args))


print(decide_args(18, 'Hello'))
print(decide_args([], {}))
print(decide_args(18, []))
