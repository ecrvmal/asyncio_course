import asyncio
from aiocsv import AsyncDictReader
import aiofiles

async def main():
    # Использует асинхронный менеджер контекста для открытия файла 'students.csv' в режиме чтения с указанием кодировки 'utf-8-sig'.
    # 'utf-8-sig' - это кодировка UTF-8 с префиксом BOM (byte order mark), который может быть использован для определения порядка байтов в текстовых файлах.
    async with aiofiles.open('students.csv', mode='r', encoding='utf-8-sig') as afp:


        reader = AsyncDictReader(afp, fieldnames=['Name', 'Surname', 'Age', 'Faculty', 'Average_Grade', 'Defunct_title'])
        # Создает экземпляр AsyncDictReader, который считывает файл afp, преобразуя каждую строку в словарь, где ключи определены в fieldnames.

        async for row in reader:
        # Использует асинхронный цикл for для итерации по строкам файла, что позволяет выполнять другие задачи во время ожидания чтения строки.

            print(row)

asyncio.run(main())