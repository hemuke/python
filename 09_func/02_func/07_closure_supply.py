#! /root/anaconda3/bin/python

def make_adder(addend):
    def adder(augend):
        return augend + addend
    return adder


p = make_adder(23)
q = make_adder(44)

print(p(100))
print(make_adder(23).__closure__)
print(make_adder(23).__closure__[0].cell_contents)
print(make_adder(23)(100))
print(q(100))
print(make_adder(44).__closure__)
print(make_adder(44).__closure__[0].cell_contents)
print(make_adder(44)(100))
