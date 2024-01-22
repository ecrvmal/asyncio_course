import asyncio


async def some_coro(num):
    # Имитируем выполнение длительной I/O зависимой операции.
    await asyncio.sleep(num)
    # Возвращаем результат работы.
    return num / 2


async def main():
    # Создаем группу задач.
    async with asyncio.TaskGroup() as tg:
        # Создаем в группе две задачи.
        task1 = tg.create_task(some_coro(1))
        task2 = tg.create_task(some_coro(2))
    print(f"Oбе задачи выполнены с результатом: {task1.result()} и {task2.result()} соответственно.")

asyncio.run(main())