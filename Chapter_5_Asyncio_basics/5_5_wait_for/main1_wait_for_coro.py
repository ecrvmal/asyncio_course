import asyncio

async def my_coro():
    await asyncio.sleep(5)
    return 'Привет мир!'

async def main():
    await asyncio.wait_for(my_coro(), timeout=3)

asyncio.run(main())

# output:
#     raise exceptions.TimeoutError() from exc
# asyncio.exceptions.TimeoutError