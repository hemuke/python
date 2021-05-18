# -*- encoding=utf-8 -*-


def test_stop_interation():
    gen = (num for num in range(10))
    while True:
        try:
            print(next(gen))
        except StopIteration as e:
            print('generator stopped')
            return

test_stop_interation()
