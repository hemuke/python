# 协程之间的数据通信
# 嵌套调用
import asyncio


async def do_sth1():
    print('方法1开始')
    await asyncio.sleep(2)
    print('one')


async def do_sth2():
    print('方法2开始')
    await asyncio.sleep(1)
    print('two')


coroutine1 = do_sth1()
coroutine2 = do_sth2()
loop = asyncio.get_event_loop()
#task1 = loop.create_task(coroutine1)
#task2 = loop.create_task(coroutine2)
#loop.run_until_complete(asyncio.gather(task1, task2))
loop.run_until_complete(asyncio.gather(coroutine1, coroutine2))

# loop.create_task(coroutine)用于创建一个task；run_until_complete的参数是一个futrue对象，当传入一个协程，其内部会自动封装成task，task是Future的子类
