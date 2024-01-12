import asyncio


async def set_future_result(future, result, delay):
    await asyncio.sleep(delay)
    future.set_result(result)


async def main():
    # Создаем объект Future, который не является корутиной
    future = asyncio.Future()

    # Запускаем задачу для установки результата Future
    asyncio.ensure_future(set_future_result(future, "Future is done", 2))

    # Используем ensure_future для запуска Future
    task_using_ensure_future = asyncio.ensure_future(future)

    # Подождем, пока Future завершится
    result = await task_using_ensure_future
    print(result)

    # Создадим еще один Future
    another_future = asyncio.Future()

    # Попробуем использовать create_task (это вызовет ошибку)
    try:
        asyncio.create_task(another_future)  # Это вызовет ошибку
    except Exception as e:
        print(f"Error when using create_task: {e}")


asyncio.run(main())


# Мы  создаем объект Future.
# Запускаем задачу, которая устанавливает результат для этого Future через 2 секунды.
# Используем asyncio.ensure_future() для запуска Future.
# Дожидаемся завершения Future и выводим его результат.
# Пытаемся использовать asyncio.create_task() с другим объектом Future(что вызовет ошибку, так
# как create_task ожидает корутину).