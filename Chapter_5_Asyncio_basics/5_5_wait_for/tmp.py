import asyncio
import time


async def coro1():
    print('starting coro1')
    for i in range(10):
        print(f'coro1  passed {time.time() - start:.3f} sec')
        await asyncio.sleep(1)
    print('completing coro1')


async def coro2():
    print('starting coro2')
    for i in range(10):
        print(f'coro2  passed {time.time() - start:.3f} sec')
        await asyncio.sleep(1)
    print('completing coro2')


async def main():
    task_coro1 = asyncio.create_task(coro1())
    task_coro2 = asyncio.create_task(coro2())
    await asyncio.wait_for(task_coro1, timeout=7)
    print('Запуск второго wait_for')  # Эта строчка не будет напечатана
    await asyncio.wait_for(task_coro2, timeout=3)

start = time.time()
asyncio.run(main())

