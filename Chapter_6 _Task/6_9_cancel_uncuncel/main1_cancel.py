import asyncio


async def main_task():
    print("Корутина main_task запустилась")     # Вывод сообщения о запуске корутины main_task
    await asyncio.sleep(5)                      # Задержка выполнения корутины main_task на 5 секунд
    print("Корутина main_task завершилась")     # Вывод сообщения о завершении корутины main_task


async def main():
    task = asyncio.create_task(main_task())     # Создание задачи из корутины main_task и запуск ее асинхронного выполнения
    await asyncio.sleep(1)                      # Задержка выполнения основной корутины main на 1 секунду
    task.cancel()                               # Отмена задачи (запрос на отмену выполнения корутины main_task)

    try:
        await task                              # Ожидание завершения задачи
    except asyncio.CancelledError:
        print("Задача отменена")                # Вывод сообщения, если задача была отменена (обработка исключения отмены задачи)

    if task.cancelled():                            # Проверка, была ли задача отменена, и вывод соответствующего сообщения
        print(f"Задача отменена - {task.cancelled()}")

asyncio.run(main())                             # Запуск асинхронного выполнения корутины main