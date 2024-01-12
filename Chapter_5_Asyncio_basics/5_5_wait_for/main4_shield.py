import asyncio


async def long_running_task():      # Определяем асинхронную функцию (корутину)
    await asyncio.sleep(10)         # Эмулируем долгую операцию, приостанавливая выполнение на 10 секунд
    return "Завершение работы защищенной корутины long_running_task() после timeout"
                                    # Возврат значения после завершения задачи


async def main():  # Основная асинхронная функция
    task = asyncio.create_task(long_running_task())
                                    # Создаем задачу, запуская корутину long_running_task()
    try:
        await asyncio.wait_for(asyncio.shield(task), timeout=5)
                                    # Ожидаем завершение задачи в течение 5 секунд
                                    # Используем shield для защиты задачи от отмены
    except TimeoutError:            # В случае превышения времени ожидания, выводим сообщение
        print("Задача не была завершена в установленное время")

        result = await task         # Все еще ждем завершения исходной задачи
        print(result)               # Печатаем результат исходной задачи


asyncio.run(main())

