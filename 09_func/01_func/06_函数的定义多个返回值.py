#! /root/anaconda3/bin/python
# 例子一
'''
把列表的所有数分成奇数和偶数
'''


def classify_number(numbers):
    odds = []
    evens = []

    for number in numbers:
        if number % 2:
            odds.append(number)
        else:
            evens.append(number)

    return odds, evens


print(classify_number([1, 2, 3, 4, 5]))


# 例子二
'''
查找列表中的最小值和最大值
'''


def lookup_min_max(numbers):
    if len(numbers) == 0:
        return

    min_num = numbers[0]
    max_num = numbers[0]

    for number in numbers[1: len(numbers)]:
        if min_num > number:
            min_num = number
        elif max_num < number:
            max_num = number

    return min_num, max_num


print(lookup_min_max([100, 10, 99, 123, 22]))
