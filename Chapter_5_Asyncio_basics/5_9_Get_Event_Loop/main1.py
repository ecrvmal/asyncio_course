import asyncio

async def my_task(n):
    print(f"Task {n} starting")
    await asyncio.sleep(1)
    print(f"Task {n} finished")

async def main():
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(my_task(i)) for i in range(5)]
    await asyncio.gather(*tasks)


asyncio.run(main())