import asyncio

async def foo():
    await asyncio.sleep(1)
    return "Завершено"

async def main():
    task = asyncio.create_task(foo())
    print("Корутина:", task.get_coro())

asyncio.run(main())
