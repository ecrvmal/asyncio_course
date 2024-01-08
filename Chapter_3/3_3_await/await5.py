#Псевдокод который ничего не делает, но наглядно демонстрирует применение await

import asyncio

async def fetch_data(url):                               # Определяем асинхронную функцию, которая имитирует получение данных из url
    await asyncio.sleep(1)                               # Производим асинхронную "паузу" на 1 секунду. Используется для имитации ожидания ответа от сервера
    return f"Data from {url}"                            # Возвращаем данные, которые представляют собой просто строку

async def main():                                        # Определяем основную асинхронную функцию
    data1 = await fetch_data("https://www.example1.com") # "Извлекаем" данные из первого URL
    data2 = await fetch_data("https://www.example2.com") # "Извлекаем" данные из второго URL

    print(f'{data1=}')                                         # Выводим полученные данные из первого URL. Здесь будет "Данные из https://www.example1.com"
    print(f'{data2=}')                                         # Выводим полученные данные из второго URL. Здесь будет "Данные из https://www.example2.com"

asyncio.run(main())