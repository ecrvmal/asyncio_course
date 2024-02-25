import asyncio

# Общий ресурс - база данных
database = []
Schritt = 0


# Функция для записи данных в базу данных
async def write_to_database(lock, data):
    async with lock:
        await asyncio.sleep(1)  # Имитация длительной операции записи
        global Schritt
        if Schritt == 2 or Schritt == 5:
            bonus = f", Счастливый номер! Бонус клиента = номер клиента {Schritt} * 100 == {Schritt*100}"
            data = data + bonus
        Schritt += 1
        database.append(data)
        # print(f'{database=}')



# Асинхронная функция для обработки запросов клиентов
async def handle_request(lock, client_id):
    data = f"Data от клиента {client_id}"

    # Измените функцию

    # Критический участок кода, требующий синхронизации
    # async with lock:
    await write_to_database(lock, data)
    print(f"Data от клиента {client_id} успешно записан в базу данных")


# Создание и запуск корутин для обработки запросов от клиентов
async def main():
    tasks = []
    lock = asyncio.Lock()
    # Измените функцию

    for i in range(10):
        tasks.append(handle_request(lock, i))
    await asyncio.gather(*tasks)


# Запуск основной асинхронной функции
asyncio.run(main())

print(*database, sep="\n")