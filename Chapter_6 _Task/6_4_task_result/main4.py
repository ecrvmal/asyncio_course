import asyncio
import random


async def my_coroutine(n):                      # Определение асинхронной корутины my_coroutine
    print(f"Корутина {n} запустилась")          # Вывод сообщения о начале работы корутины с учетом переданного аргумента n
    sleep_time = random.randint(1, 10)          # Генерация случайного числа от 1 до 10 и сохранение его в переменную sleep_time
    await asyncio.sleep(sleep_time)             # Приостановка выполнения корутины на sleep_time секунд
    print(f"Корутина {n} завершилась после {sleep_time} секунд")    # Вывод сообщения о завершении работы корутины с указанием времени приостановки
    return sleep_time                           # Возвращение значения sleep_time в качестве результата выполнения корутины


async def main():                                                       # Определение основной асинхронной функции main
    tasks = [asyncio.create_task(my_coroutine(i)) for i in range(5)]    # Создание списка задач с корутинами my_coroutine с разными аргументами
    await asyncio.sleep(1)                                              # Приостановка выполнения основной функции на 1 секунду
    print("Функция main продолжает работу")                             # Вывод сообщения о продолжении выполнения функции main
    timeout_list = [random.randint(1, 3) for _ in range(5)]             # Создание списка таймаутов с случайными числами от 1 до 3
    for i, task in enumerate(tasks):                                    # Цикл по всем задачам из списка tasks
        try:
            await asyncio.wait_for(task, timeout=timeout_list[i])       # Ожидание завершения задачи task с соответствующим таймаутом из списка timeout_list
            result = task.result()                                      # Получение результата выполнения корутины
            print(f"Результат выполнения корутины {i}: {result}")       # Вывод результата выполнения корутины с указанием индекса задачи
        except asyncio.TimeoutError:
            print(f"Задача {i} не была завершена в указанное время (таймаут: {timeout_list[i]} сек.).")   # Обработка исключения при превышении времени ожидания завершения задачи

asyncio.run(main())                                                     # Запуск асинхронной функции main с помощью asyncio.run