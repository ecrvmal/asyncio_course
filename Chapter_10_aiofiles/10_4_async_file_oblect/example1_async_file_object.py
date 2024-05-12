import asyncio
import aiofiles

async def main():
    # f - это асинхронный файловый объект
    async with aiofiles.open('myfile.txt', mode='r') as f:

        # Асинхронно читаем содержимое файла
        contents = await f.read()
    print(contents)

asyncio.run(main())

