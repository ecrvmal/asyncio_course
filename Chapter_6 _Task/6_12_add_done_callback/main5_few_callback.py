import asyncio


def callback1(task):
    print('Callback 1: Task completed!')
    print('Result:', task.result())


def callback2(task):
    print('Callback 2: Task completed!')
    print('Result:', task.result())


async def my_coro():
    return 42


async def main():
    # Создание задачи
    task = asyncio.create_task(my_coro())

    # Добавление callback-ов к задаче
    task.add_done_callback(callback1)
    task.add_done_callback(callback2)

    # Ожидание завершения задачи
    await task

# Запуск основного асинхронного корутина
asyncio.run(main())

# Callback 1: Task completed!
# Result: 42
# Callback 2: Task completed!
# Result: 42