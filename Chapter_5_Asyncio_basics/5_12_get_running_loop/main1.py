import asyncio

async def my_task():
    print("Running my task")

async def main():
    loop = asyncio.get_running_loop()
    loop.create_task(my_task())
    print(f"{id(loop)}")
    await asyncio.sleep(1)

asyncio.run(main())
