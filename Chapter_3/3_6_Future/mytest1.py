import asyncio

async def f2(n):
    future=asyncio.Future()
    print('starting f2')
    await asyncio.sleep(2)
    future.set_result('F2 calculated result')
    return future


async def f1():
    future = await f2(2)
    print(await future)

asyncio.run(f1())

