# Чтобы запустить корутину в asyncio, необходимо использовать функцию asyncio.run().
# Эта функция запускает цикл событий и выполняет все задачи, добавленные в цикл.
# Вот пример того, как запустить корутину my_coroutine() из предыдущего примера:

import asyncio

async def my_coroutine(duration):       # Объявляем корутину, которая принимает в качестве аргумента продолжительность ожидания
    print("Начинаем my_coroutine")      # Выводим информационное сообщение о начале выполнения корутины
    await asyncio.sleep(duration)       # Приостанавливаем выполнение текущей корутины на указанное количество секунд.
                                        # asyncio.sleep используется для имитации длительной операции
    print("Завершаем my_coroutine")     # Выводим информационное сообщение о завершении выполнения корутины
    return "Результат"                  # Возвращаем результат выполнения корутины


asyncio.run(my_coroutine(1))            # Запускаем корутину с задержкой в 1 секунду. asyncio.run обеспечивает выполнение корутины и ожидание её завершения