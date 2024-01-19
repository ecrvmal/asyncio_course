import asyncio

async def my_coroutine():
    print(f"Имя задачи: {asyncio.current_task().get_name()}")

async def main():
    task = asyncio.create_task(my_coroutine(), name="my_task")
    await task

asyncio.run(main())