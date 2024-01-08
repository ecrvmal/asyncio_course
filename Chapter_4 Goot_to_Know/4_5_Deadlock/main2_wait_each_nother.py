# пример: Новая корутина: Ожидает основную корутину.
# Основная корутина: Ожидает новую корутину.


import asyncio


# принимает задачу и ждет ее завершения
async def task(other):                               # Объявление асинхронной функции task, которая принимает объект other (другую задачу)
    print(f'ожидание задачи: {other.get_name()}')    # Выводим сообщение о том, что мы ожидаем завершения другой задачи.
                                                     # Метод get_name() используется для получения имени задачи
    await other                                      # Используем await для приостановки выполнения текущей задачи до завершения другой задачи


async def main():                                    # Объявление основной асинхронной функции main
    task1 = asyncio.current_task()                   # Получаем текущую задачу с помощью метода current_task() из модуля asyncio
    task2 = asyncio.create_task(task(task1))         # Создаем новую задачу, используя метод create_task() из модуля asyncio.
                                                     # В эту задачу передаем другую задачу (task1)
                                                     # Выполняем задачу, которая будет ожидать task2
    await task(task2)                                # Приостанавливаем выполнение текущей задачи до завершения задачи task2

asyncio.run(main())

# Вывод:
#
# ожидание задачи: Task-2
# ожидание задачи: Task-1
# ...
# ...
# ...
# deadlock / бесконечное ожидание корутины / зависание приложения