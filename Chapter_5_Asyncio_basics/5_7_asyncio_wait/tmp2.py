# Сколько задач завершились с исключением?
import asyncio


async def my_coro(name, delay):
    await asyncio.sleep(delay)
    if name == "task_1":
        raise Exception("task_2 exception")
    return f"{name} completed"


async def main():
    tasks = [asyncio.create_task(my_coro(f"task_{i}", 0.1 + i / 10)) for i in range(3)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    exceptions = [t.exception() is not None for t in done]
    print(exceptions.count(True))


result = asyncio.run(main())