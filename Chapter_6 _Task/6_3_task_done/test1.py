# Напишите код, который симулирует асинхронную загрузку файлов с проверкой статуса задачи каждую секунду.
# У вас есть коллекция из 20 файлов различных типов и размеров, которые нужно "загрузить".
#
# Исходные данные:
# Словарь files, где ключ — это имя файла, а значение — размер файла в мегабайтах.
# Фиксированная скорость сети — 8 мегабайт в секунду
# Расчет времени загрузки: Программа должна вычислять время, необходимое для скачивания каждого файла,
# исходя из его размера и скорости сети. Время загрузки рассчитывается как размер файла / скорость сети.
# Используйте  asyncio.sleep() для имитации загрузки файлов по формуле выше.
#
# Цели Задачи:
# Разработать логику для регулярной проверки и отображения статуса загрузки каждого файла, каждые 1 сек.


import asyncio

# Словарь файлов и их размеров
files = {
    "file1.mp4": 32,
    "image2.png": 24,
    "audio3.mp3": 16,
    "document4.pdf": 8,
    "archive5.zip": 40,
    "video6.mkv": 48,
    "presentation7.pptx": 12,
    "ebook8.pdf": 20,
    "music9.mp3": 5,
    "photo10.jpg": 7,
    "script11.py": 3,
    "database12.db": 36,
    "archive13.rar": 15,
    "document14.docx": 10,
    "spreadsheet15.xls": 25,
    "image16.gif": 2,
    "audioBook17.mp3": 60,
    "tutorial18.mp4": 45,
    "code19.zip": 22,
    "profile20.jpg": 9
}


async def download_file(file_name, file_size):
    time_to_load = file_size / 8.
    print(f'Начинается загрузка файла: {file_name}, его размер {file_size} мб, время загрузки составит {time_to_load} сек')
    await asyncio.sleep(time_to_load)
    print(f'Загрузка завершена: {file_name}')


async def monitor_tasks(tasks):
    checking = True
    while checking:
        checking = False
        for task in tasks:
            name = task.get_name()
            status = task.done()
            if status:
                print(f'Задача {name}: завершена, Статус задачи {status}')
            else:
                print(f'Задача {name}: в процессе, Статус задачи {status}')
                checking = True
        await asyncio.sleep(1)
    for task in tasks:
        name = task.get_name()
        print(f'Задача {name}: завершена, Статус задачи {status}')
    print('Все файлы успешно загружены')
    return


async def main():
    tasks = []

    for k, v in files.items():
        task = asyncio.create_task(download_file(k, v), name=k)
        tasks.append(task)
    monitor_tasks1 = asyncio.create_task(monitor_tasks(tasks))
    await monitor_tasks1
    for el in tasks:
        await el


asyncio.run(main())