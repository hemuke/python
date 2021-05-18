import random

# (0.0~1.0)
print(random.random())

# (5.0~9.0)
print(random.uniform(5, 9))

# [5~9]
print(random.randint(5, 9))

lst = ['A', 'B', 'C', 'D']
print(random.choice(lst))

lst = ['A', 'B', 'C', 'D']
print(random.sample(lst, 2))

##练习题 随机生成验证码
def rand_num():
    return str(random.randint(0,9))


def rand_upper():
    return chr(random.randint(65, 90))


def rand_lower():
    return chr(random.randint(97, 122))


def rand_verify_code(n=4):
    lst = []
    for i in range(n):
        which = random.randint(1, 3)
        if which == 1:
            s = rand_num()
        elif which == 2:
            s = rand_upper()
        else:
            s = rand_lower()
        lst.append(s)
    return "".join(lst)

print(rand_verify_code())
