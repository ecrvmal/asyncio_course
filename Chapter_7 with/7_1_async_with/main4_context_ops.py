import asyncio


class AsyncTransaction:
    async def __aenter__(self):                             # Метод для выполнения асинхронной операции перед началом контекста
        print("Starting transaction")
        await asyncio.sleep(0.5)

    async def __aexit__(self, exc_type, exc_val, exc_tb):   # Метод для выполнения асинхронной операции после завершения контекста
        print("Ending transaction")
        await asyncio.sleep(0.5)


async def perform_transaction():
    async with AsyncTransaction():                          # Используем async with для корректного выполнения асинхронных операций перед началом и после завершения контекста
        print("Performing transaction operations")          # Выводим сообщение о выполнении операций в контексте транзакции
        await asyncio.sleep(1)                              # Имитируем асинхронную операцию внутри транзакции


asyncio.run(perform_transaction())

