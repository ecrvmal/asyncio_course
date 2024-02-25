import asyncio

async def protected_section(lock, task_id):
    async with lock:                                                # Используем async with для корректного захвата и освобождения блокировки
        print(f'Task {task_id} has entered the protected section')  # Выводим информацию о входе в критическую секцию
        await asyncio.sleep(1)                                      # Имитируем асинхронную операцию в критической секции
        print(f'Task {task_id} has left the protected section')     # Выводим информацию об выходе из критической секции

async def main():   
    lock = asyncio.Lock()                                           # Создаем асинхронную блокировку
    tasks = [protected_section(lock, i) for i in range(3)]          # Создаем список задач, которые будут использовать блокировку
    await asyncio.gather(*tasks)                                    # Запускаем все задачи одновременно


asyncio.run(main())                                                 # Запускаем асинхронную функцию main