import asyncio

async def f2(n):
    future=asyncio.Future()
    print('starting f2')
    await asyncio.sleep(2)
    print('ending f2')
    return n*2


async def f1():
    future = asyncio.ensure_future(f2(2))
    result = await future
    print(f'{result=}')

asyncio.run(f1())

