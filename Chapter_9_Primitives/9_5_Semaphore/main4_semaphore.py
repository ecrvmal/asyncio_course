import asyncio

# Создаем два семафора с максимальным количеством зеленых светофоров равным 2
sem1 = asyncio.Semaphore(2)                      # Ограничивает количество одновременно выполняемых задач до двух
sem2 = asyncio.Semaphore(2)                      # Еще один семафор, который также ограничивает количество одновременно выполняемых задач до двух

async def task(id):
    async with sem1, sem2:                       # Используется для управления доступом к критической секции кода и гарантии безопасности в многопоточной среде
        print(f'Задача {id} начала выполнение')  # Информируем о начале выполнения задачи
        await asyncio.sleep(1)                   # Имитируем задержку, позволяющую другим задачам выполниться
        print(f'Задача {id} завершила выполнение')  # Информируем о завершении задачи


async def main():
    tasks = [task(i) for i in range(5)]  # Создаем список задач для выполнения
    await asyncio.gather(*tasks)         # Используется для выполнения всех задач асинхронно

# Запускаем все задачи
asyncio.run(main())