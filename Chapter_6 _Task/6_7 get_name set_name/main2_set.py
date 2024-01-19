import asyncio

async def my_coroutine():
    print(f"Имя задачи до изменения: {asyncio.current_task().get_name()}")
    asyncio.current_task().set_name("new_name")
    print(f"Имя задачи после изменения: {asyncio.current_task().get_name()}")

async def main():
    task = asyncio.create_task(my_coroutine(), name="my_task")
    await task

asyncio.run(main())

# output:
# Имя задачи до изменения: my_task
# Имя задачи после изменения: new_name
