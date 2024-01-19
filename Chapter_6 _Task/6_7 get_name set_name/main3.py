import asyncio
import aiohttp


async def download_file(url):  # Определение асинхронной функции для скачивания файла по URL
    async with aiohttp.ClientSession() as session:  # Создание асинхронного HTTP-соединения с помощью aiohttp.ClientSession
        async with session.get(url) as response:  # Отправка асинхронного GET-запроса по указанному URL
            filename = response.headers.get("content-disposition")  # Извлечение имени файла из заголовков ответа
            if filename:
                filename = filename.split("filename=")[1]
            task = asyncio.current_task()  # Установка имени текущей задачи для удобства отслеживания
            task.set_name(f"Downloading {filename}")
            with open(filename, "wb") as f:  # Открытие файла для записи бинарных данных
                while True:
                    chunk = await response.content.read(1024)  # Чтение содержимого ответа по частям и запись в файл
                    if not chunk:
                        break
                    f.write(chunk)
            task.set_name(f"Downloaded {filename}")  # Обновление имени текущей задачи после завершения скачивания


async def main():  # Определение асинхронной функции main для управления задачами скачивания
    urls = [
        "<https://www.example.com/file1.txt>",
        "<https://www.example.com/file2.txt>",
        "<https://www.example.com/file3.txt>"
    ]

    tasks = [asyncio.create_task(download_file(url)) for url in
             urls]  # Создание задач скачивания для каждого URL из списка
    await asyncio.gather(*tasks)  # Ожидание завершения всех задач скачивания


asyncio.run(main())  # Запуск асинхронной функции main