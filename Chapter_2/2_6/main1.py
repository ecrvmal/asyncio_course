import asyncio

async def task1():
    await asyncio.sleep(1)
    print(f'Task1 completed')

async def task2():
    await asyncio.sleep(2)
    print(f'Task2 completed')

async def main():
    tasks = [task1(), task2()]
    await asyncio.gather(*tasks)

asyncio.run(main())





