# 协程之间的数据通信
# 嵌套调用
import asyncio


async def compute(x, y):
    print('计算x +y => {0}+{1}'.format(x, y))
    await asyncio.sleep(1)
    # 不能用time.sleep 因为他不是返回一个协程的对象
    return x + y


async def get_sum(x, y):
    rest = await compute(x, y)
    #rest = compute(x, y)
    print('{0} + {1} = {2}'.format(x, y, rest))

# 拿到事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(get_sum(1, 2))
loop.close()
