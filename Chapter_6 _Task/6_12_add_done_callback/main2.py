import asyncio


async def async_operation():                            # Асинхронная функция, имитирующая асинхронную операцию
    print("Асинхронная операция началась...")
    await asyncio.sleep(2)
    print("Асинхронная операция завершена.")
    return "Результат асинхронной операции"


def on_completion(task):                                # Callback-функция, которая вызывается по завершении асинхронной операции
    result = task.result()                              # Получение результата из задачи
    print(f"Callback функция вызвана. Получен результат: {result}")


async def main():                                       # Основная асинхронная функция
    task = asyncio.create_task(async_operation())       # Создание задачи из асинхронной функции async_operation
    task.add_done_callback(on_completion)               # Регистрация callback-функции для выполнения по завершении асинхронной операции
    await task                                          # Ждем завершения задачи


asyncio.run(main())                                     # Запуск основной асинхронной функции

# output:
# Асинхронная операция началась...
# Асинхронная операция завершена.
# Callback функция вызвана. Получен результат: Результат асинхронной операции
