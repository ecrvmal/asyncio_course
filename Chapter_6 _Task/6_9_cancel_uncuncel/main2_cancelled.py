import asyncio


async def main_task():                                   # Определение асинхронной функции main_task, которая представляет собой корутину
    print("Корутина main_task запустилась")              # Вывод сообщения о запуске корутины main_task
    await asyncio.sleep(5)                               # Ожидание (приостановка выполнения корутины) на 5 секунд
    print("Корутина main_task завершилась")              # Вывод сообщения о завершении корутины main_task


async def main():                                        # Определение асинхронной функции main, которая является основной точкой входа
    task = asyncio.create_task(main_task())              # Создание асинхронной задачи из корутины main_task
    await asyncio.sleep(1)                                    # Отмена задачи
    await asyncio.sleep(2)                               # Ожидание (приостановка выполнения корутины) на 2 секунды
    if task.cancelled():                                 # Проверка, была ли задача отменена, и вывод соответствующего сообщения
        print(f"Задача отменена - {task.cancelled()}")


asyncio.run(main())                                      # Запуск асинхронной функции main с использованием функции asyncio.run