import asyncio

async def my_coroutine(seconds):
    # Определяем асинхронную функцию-корутину, которая будет выполняться указанное количество секунд
    print(f'Корутина {asyncio.current_task().get_name()} начала работу и будет выполняться {seconds} секунд')
    try:
        # Ожидаем указанное количество секунд
        await asyncio.sleep(seconds)
    except asyncio.CancelledError:
        # Обрабатываем исключение, если корутина была отменена
        print(f'Корутина {asyncio.current_task().get_name()} была отменена')
        raise
    # Проверяем, отменяется ли сейчас задача, и выводим соответствующее сообщение
    if asyncio.current_task().cancelling():
        print(f'Корутина {asyncio.current_task().get_name()} сейчас отменяется')

async def main():
    # Создаем две асинхронные задачи, используя нашу корутину с разными аргументами
    task_1 = asyncio.create_task(my_coroutine(5))
    task_2 = asyncio.create_task(my_coroutine(10))
    # Ожидаем 2 секунды
    await asyncio.sleep(2)
    # Отменяем первую задачу
    task_1.cancel()
    # Дожидаемся завершения обеих задач, игнорируя исключения (return_exceptions=True)
    await asyncio.gather(task_1, task_2, return_exceptions=True)
    # Проверяем, была ли отменена первая задача, и выводим соответствующее сообщение
    if task_1.cancelled():
        print(f'Задача {task_1.get_name()} была отменена, её флаг отмены {task_1.cancelled()}')
    # Проверяем, была ли отменена вторая задача, и выводим соответствующее сообщение
    if task_2.cancelled():
        print(f'Задача {task_2.get_name()} была отменена, её флаг отмены {task_2.cancelled()}')

# Запускаем главную функцию
asyncio.run(main())

