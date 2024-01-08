import asyncio
import asyncio
import time


async def coro_1():
    print('coro_1 started')
    await asyncio.sleep(1)
    print('coro_1 says, hello coro_2!')


async def coro_2():
    print('coro_2 started')
    await asyncio.sleep(2)
    print('coro_2 says, hello coro_1!')


async def main():
    task1 = asyncio.create_task(coro_1())
    task2 = asyncio.create_task(coro_2())
    # time.sleep(3)
    # or
    # await asyncio.gather(task1, task2)
    # or
    # await task1
    # await task2
    # or
    # await coro_1()
    # await coro_2()

asyncio.run(main())