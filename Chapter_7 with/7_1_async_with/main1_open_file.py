import aiofiles
import asyncio

async def read_file(file_name):
    async with aiofiles.open(file_name, 'r') as file:       # Используем async with для открытия файла асинхронно
        contents = await file.read()                        # Читаем содержимое файла асинхронно
        print(contents)                                     # Выводим содержимое файла

asyncio.run(read_file('example.txt'))                       # Запускаем асинхронную функцию чтения файла