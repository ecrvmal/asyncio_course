import asyncio

async def task_coroutine(num):
    await asyncio.sleep(1)
    print(f"Задача {num} выполнена")
    return f'Task_{num}'

async def main():
    tasks = [asyncio.create_task(task_coroutine(x)) for x in range(5)]
    all_tasks = asyncio.all_tasks()
    print(f"Количество задач: {len(all_tasks)}")
    await asyncio.gather(*tasks)
    for task in all_tasks:
        print(task)               # result is not awailable
        if task.done():              # main task is not done
            print(task.result())


    for task in tasks:
        print(task.result())


asyncio.run(main())

