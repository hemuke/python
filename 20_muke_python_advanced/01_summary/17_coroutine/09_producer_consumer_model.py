# -*- encoding=utf-8 -*-

"""
不需要关注临界值
"""
import time


def consumer():
    print("我是next(gen)激活输出的")
    cnt = yield
    while True:
        if cnt <= 0:
            print('暂停、让出CPU')
            cnt = yield cnt
        cnt -= 1
        print('consumer consum 1 cnt. cnt =', cnt) 
        time.sleep(1)


def producer(cnt):    
    gen = consumer()
    # 激活生成器
    next(gen)
    gen.send(cnt)
    while True:
        cnt += 5
        print('producer producer 5 cnt. cnt = ', cnt)
        # 调度消费者
        current = int(time.time())
        if current % 7 ==0:
            cnt = gen.send(cnt)
        else:
            time.sleep(1)


if __name__ == '__main__':

    producer(0)
