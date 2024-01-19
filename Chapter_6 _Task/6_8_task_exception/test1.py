import asyncio


async def my_coro():
    await asyncio.sleep(1)
    raise ValueError("--- Value error Exception ---")

async def main():
    task = asyncio.create_task(my_coro())
    await asyncio.sleep(0.5)
    try:
        await task
    except Exception as e:
        print(f'exception: {e=}')
    my_exception = task.exception()
    if my_exception:
        print(my_exception)

asyncio.run(main())

