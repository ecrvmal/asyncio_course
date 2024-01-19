import asyncio


async def failing_coroutine():  # Определение асинхронной функции, которая имитирует ошибку
    await asyncio.sleep(1)  # Асинхронное ожидание на 1 секунду
    raise ValueError("Возникла ошибка в корутине failing_coroutine()")  # Генерируем исключение ValueError


async def successful_coroutine():  # Определение асинхронной функции, которая успешно завершает свою работу
    await asyncio.sleep(1)  # Асинхронное ожидание на 1 секунду
    print("Успешное выполнение")  # Вывод сообщения об успешном выполнении


async def main():  # Определение основной асинхронной функции
    tasks = [asyncio.create_task(failing_coroutine()),
             asyncio.create_task(successful_coroutine())]  # Создание списка задач (корутин) для выполнения
    try:  # Обработка исключений, возникающих во время выполнения корутин
        await asyncio.gather(*tasks)  # Запуск всех задач одновременно
    except ValueError as _ex:  # Ловим исключение ValueError, если возникло
        print(_ex)  # Выводим информацию об исключении

    for i, task in enumerate(tasks, start=1):  # Перебираем все задачи и выводим результат их выполнения
        exc = task.exception()  # Получаем исключение из задачи, если оно возникло
        if exc:  # Если исключение возникло
            print(f"Задача {task.get_name()}: Исключение - {exc}")  # Выводим информацию об исключении
        else:
            print(f"Задача {task.get_name()}: Успешно выполнена")  # В противном случае сообщаем об успешном выполнении


asyncio.run(main())  # Запуск асинхронной функции main()