import asyncio

async def long_coro():
    print("starting long coro")
    await asyncio.sleep(7)
    print("ending long coro")
    return "Long-run coroutine finished work"

async def main():
    task1 = asyncio.create_task(long_coro())
    try:
        result = await asyncio.wait_for(asyncio.shield(task1), timeout=10)
        print(f'{result}')
    except asyncio.TimeoutError:
        print('timeout exceed')
        result = None
    if not result:
        result = await task1
        print(f'{result=}')

asyncio.run(main())

# printout:
#
# starting long coro
# timeout exceed
# ending long coro
# result='Long-run coroutine finished work'
#
# Process finished with exit code 0