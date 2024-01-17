import asyncio

# Определяем асинхронную функцию (корутину), которая "спит" на заданное количество секунд
async def my_coroutine(seconds):
    print(f'Корутина будет спать {seconds} секунд')       # Выводим сообщение о том, что корутина собирается "спать"
    await asyncio.sleep(seconds)                          # Используем asyncio.sleep для имитации блокирующей операции. Оператор await позволяет корутине "спать" без блокировки всего приложения
    print(f'Корутина проснулась после {seconds} секунд')  # Выводим сообщение о том, что корутина "проснулась"

# Определяем главную корутину, которая будет управлять другими корутинами
async def main():
    task1 = asyncio.create_task(my_coroutine(1))  # Создаем задачу из корутины, которая "спит" 1 секунду. Задача начнет выполняться, когда будет готова
    task2 = asyncio.create_task(my_coroutine(2))  # Создаем задачу из корутины, которая "спит" 2 секунды. Задача начнет выполняться, когда будет готова

    print('Задачи созданы')     # Выводим сообщение о том, что задачи созданы
    await task1                 # Ждем, пока задача task1 не завершится
    await task2                 # Ждем, пока задача task2 не завершится
    print('Задачи завершены')   # Выводим сообщение о том, что задачи завершены

asyncio.run(main())