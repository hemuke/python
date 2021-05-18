# 如果一个对象可以在 await 语句中使用，那么它就是 可等待 对象。许多 asyncio API 都被设计为接受可等待对象。
# 可等待 对象有三种主要类型: 协程, 任务 和 Future.
# Future

"""
Future 对象
Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果。
当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。
在 asyncio 中需要 Future 对象以便允许通过 async/await 使用基于回调的代码。
通常情况下 没有必要 在应用层级的代码中创建 Future 对象。
Future 对象有时会由库和某些 asyncio API 暴露给用户，用作可等待对象:
"""
import asyncio


async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )


asyncio.run(main())
