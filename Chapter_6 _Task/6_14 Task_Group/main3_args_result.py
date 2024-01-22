import asyncio


async def coro(value):
    await asyncio.sleep(1)
    return value * 100


async def main():
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(coro(i)) for i in range(1, 11)]
        for el in tasks: print(el)

    for task in tasks:
        print(task)
        print(task.result())

asyncio.run(main())