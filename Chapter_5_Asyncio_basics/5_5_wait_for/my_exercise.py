import asyncio

async def coro1():
    print('starting coro1')
    for i in range(10):
        print(f'coro1  passed {i} sec')
        await asyncio.sleep(1)
    print('completing coro1')

async def coro2():
    print('starting coro2')
    for i in range(10):
        print(f'coro2  passed {i} sec')
        await asyncio.sleep(1)
    print('completing coro2')

async def main():
    task_coro1 = asyncio.create_task(coro1())
    task_coro2 = asyncio.create_task(coro2())
    await asyncio.wait_for(task_coro1, timeout=7)
    await asyncio.wait_for(task_coro2, timeout=3)

asyncio.run(main())
