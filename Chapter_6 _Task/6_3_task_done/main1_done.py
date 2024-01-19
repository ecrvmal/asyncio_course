import asyncio

async def coro():
    print('coro started')
    await asyncio.sleep(2)
    print('coro completed')
    return f'result of coro'

async def main():
    task = asyncio.create_task(coro())
    print(f'task status done = {task.done()}')
    print(f'task created and set to event loop')
    await task
    print(f'task status done = {task.done()}')
    result = task.result()
    print(f'{result=}')

asyncio.run(main())
