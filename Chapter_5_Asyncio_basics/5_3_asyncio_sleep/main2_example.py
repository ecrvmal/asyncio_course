import asyncio

async def coroutine1():
    print("Coroutine 1 started")
    await asyncio.sleep(1)
    print("Coroutine 1 resumed")

async def coroutine2():
    print("Coroutine 2 started")
    await asyncio.sleep(2)
    print("Coroutine 2 resumed")

async def main():
    task1 = asyncio.create_task(coroutine1())
    await task1
    task2 = asyncio.create_task(coroutine2())
    await task2

asyncio.run(main())

# result:
# Coroutine 1 started
# Coroutine 1 resumed
# Coroutine 2 started
# Coroutine 2 resumed
