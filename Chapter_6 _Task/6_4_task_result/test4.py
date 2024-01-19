import asyncio
import random


async def my_coro(num: int) -> str:
    time_to_run = random.randint(1,10)
    print(f' coro-{num} started, need: {time_to_run} sec')
    await asyncio.sleep(time_to_run)
    print(f' coro-{num} completed')
    return f'coro {num} result'

async def main():
    tasks = [asyncio.create_task(my_coro(i)) for i in range(5)]
    timeout_list = [random.randint(1,4) for _ in range(5)]
    for i, task in enumerate(tasks):
        try:
            await asyncio.wait_for(task, timeout=timeout_list[i])
            result = task.result()
            print(f'result of {task.get_name()}  is: {task.result()}')
        except asyncio.TimeoutError:
            print(f"Задача {i} не была завершена в указанное время (таймаут: {timeout_list[i]} сек.).")

asyncio.run(main())

