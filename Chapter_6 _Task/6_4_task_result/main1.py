import asyncio

async def my_coro() -> str :
    print(f'my_coro started')
    await asyncio.sleep(4)
    print(f'my_coro completed')
    return f'this is result of "my_coro" execution'


async def main() -> None:
    task = asyncio.create_task(my_coro())
    print('task started')
    await asyncio.sleep(2)
    print('main still alive')
    await task
    print(f'result of {task.get_name()}   : {task.result()}')

asyncio.run(main())
