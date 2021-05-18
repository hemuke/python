import asyncio


async def do_sth(x):
    """ 定义协程函数 """
    print('真正等待中: {0}'.format(x))
    await asyncio.sleep(x)
    # await后边要跟异步函数或协程。async
    # 声明的函数为异步函数，asyncio.sleep(x)会返回一个协程，而time.sleep(5)只是简单的模块调用

# 判断是否为协程函数
print(asyncio.iscoroutinefunction(do_sth))

coroutine = do_sth(5)
# 事件的循环队列
loop = asyncio.get_event_loop()
print("1", loop)
# 注册任务
task = loop.create_task(coroutine)
print("2", task)
# 等待协程任务执行结束
loop.run_until_complete(task)
print("3", task)
