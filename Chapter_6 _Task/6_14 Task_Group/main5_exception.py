import asyncio


# Корутина для создания задач
async def coro():
    # Получение имени выполняемой задачи
    name = asyncio.current_task().get_name()
    # Сообщение о начале работы задачи
    print(f'{name} начала свою работу!')
    # Имитация выполнения I/O операции
    await asyncio.sleep(3)
    # Сообщение о завершении работы задачи
    print(f'{name} завершена!')


# Корутина для подъема исключений
async def ex_coro():
    await asyncio.sleep(1)
# 1) Поведение характерное для обработки KeyboardInterrupt и SystemExit
# Повторный вызов изначального исключения
#     print('ex_coro поднимает исключение KeyboardInterrupt')
#     raise KeyboardInterrupt
# 2) Поведение характерное для обработки других исключений (кроме asyncio.CancelledError)
# Исключения группируются в ExceptionGroup
    print('ex_coro поднимает исключение Exсeption')
    raise Exception('Что-то пошло не так!(((')


# Базовая корутина
async def main():
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(coro(), name=f'Задача_0{i}') for i in range(1, 4)]
        # Создание задачи, имитирующей возникновение исключения
        task_ex = group.create_task(ex_coro())

    # какой-то код, который не будет выполнен


asyncio.run(main())