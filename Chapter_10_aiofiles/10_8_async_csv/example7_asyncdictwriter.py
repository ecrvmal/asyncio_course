import asyncio
import aiofiles
from aiocsv import AsyncDictWriter


async def write_csv_rows():
    async with aiofiles.open('output.csv', mode='w', newline='') as file:
        # Создает экземпляр AsyncDictWriter, который будет записывать данные в файл, преобразуя каждый словарь в строку CSV.
        # Ключи словаря соответствуют полям CSV файла ("Name", "Age", "City").
        writer = AsyncDictWriter(file, fieldnames=["Name", "Age", "City"],)

        # Асинхронно записывает заголовки в файл CSV. Этот метод используется для создания первой строки файла,
        # которая содержит названия полей.
        await writer.writeheader()

        # Определяет список словарей, каждый из которых будет записан в файл как отдельная строка.
        rows = [
            {"Name": "John", "Age": 30, "City": "New York"},
            {"Name": "Jane", "Age": 25, "City": "Los Angeles"},
            {"Name": "Bob", "Age": 35, "City": "Chicago"},
        ]

        # Асинхронно записывает все строки (словари) из списка rows в файл CSV.
        await writer.writerows(rows)

asyncio.run(write_csv_rows())

