import aiofiles
import asyncio


async def read_file_line_by_line(file_path):                    # Определяем асинхронную функцию read_file_line_by_line, которая принимает путь к файлу
    async with aiofiles.open(file_path, mode='r') as file:      # Используем async with для асинхронного открытия файла с помощью aiofiles.open
        async for line in file:                                 # Используем async for для итерации по строкам файла
            print(line.strip())                                 # Выводим каждую строку на экран без символа перевода строки (strip удаляет пробелы и символы перевода строки)
            # print(line)

async def main():                                               # Определяем асинхронную функцию main, которая будет запускать нашу функцию чтения файла
    file_path = 'example.txt'                                   # Задаем путь к файлу
    await read_file_line_by_line(file_path)                     # Вызываем асинхронную функцию чтения файла и ждем ее завершения с помощью await


asyncio.run(main())                                             # Запускаем асинхронную функцию main с помощью asyncio.run
