import asyncio

# Создание объекта Lock
lock = asyncio.Lock()

# Определение корутины "my_task" с аргументом "task_id"
async def my_task(task_id):

    # Вывод сообщения о том, что задача ждет блокировки
    print(f"Задача {task_id} ожидает блокировки с помощью Lock")

    # Ожидание получения блокировки
    await lock.acquire()

    try:
        # Вывод сообщения о том, что задача получила блокировку
        print(f"Задача {task_id} получила блокировку")

        # Остановка выполнения корутины на 2 секунды
        await asyncio.sleep(2)

    finally:
        # Вывод сообщения о том, что задача освобождает блокировку
        print(f"Задача {task_id} блокировка снята")

        # Освобождение блокировки
        lock.release()

# Определение главной корутины "main"
async def main():

    # Создание списка задач из 5 вызовов "my_task"
    tasks = [asyncio.create_task(my_task(i)) for i in range(5)]

    # Ожидание выполнения всех задач
    await asyncio.gather(*tasks)

# Запуск главной корутины
asyncio.run(main())

# Задача 0 ожидает блокировки с помощью Lock
# Задача 0 получила блокировку
# Задача 1 ожидает блокировки с помощью Lock
# Задача 2 ожидает блокировки с помощью Lock
# Задача 3 ожидает блокировки с помощью Lock
# Задача 4 ожидает блокировки с помощью Lock
# Задача 0 блокировка снята
# Задача 1 получила блокировку
# Задача 1 блокировка снята
# Задача 2 получила блокировку
# Задача 2 блокировка снята
# Задача 3 получила блокировку
# Задача 3 блокировка снята
# Задача 4 получила блокировку
# Задача 4 блокировка снята
