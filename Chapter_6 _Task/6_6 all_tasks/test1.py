import asyncio

async def my_coro(num: int) -> str:
    print(f'task-{num} is running')
    await asyncio.sleep(2)
    return f'task-{num} result'


async def main():
    tasks = [asyncio.create_task(my_coro(i)) for i in range(1,6)]
    tasks_list = asyncio.all_tasks()
    for el in tasks_list:
        print(el)
    print(f'total tasks : {len(tasks_list)}')
    await asyncio.gather(*tasks)

    for el in tasks_list:
        print(el)
        if el.done():
            print(el.result())


asyncio.run(main())