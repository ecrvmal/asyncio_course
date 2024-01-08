import asyncio

bank_account = 1000                                   # Инициализация банковского счета

async def withdraw_money(lock, amount):                     # Асинхронная функция для снятия денег
    global bank_account                               # Объявление bank_account как глобальной переменной, чтобы изменить значение вне функции
    async with lock:
        if bank_account >= amount:                        # Проверка наличия достаточных средств на счете
            print(f"Снятие {amount}р успешно")            # Вывод сообщения об успешном снятии средств
            await asyncio.sleep(1)                        # Используется асинхронная задержка, чтобы имитировать обработку банковской операции
            bank_account -= amount                        # Вычитание суммы снятия из общего банковского счета
        else:
            print("not enough money")

async def main():                                     # Главная асинхронная функция
    lock = asyncio.Lock()
    task1 = asyncio.create_task(withdraw_money(lock, 900))  # Создание задачи для асинхронного снятия средств.
                                                      # Используется asyncio.create_task для создания и запуска корутины без блокировки основного потока
    task2 = asyncio.create_task(withdraw_money(lock, 900))  # То же самое для второй операции снятия денег

    await asyncio.gather(task1, task2)                  # asyncio.gather используется для запуска и ожидания завершения всех задач.
                                                        # Позволяет запускать несколько задач одновременно

    print(f'Остаток средств {bank_account}р')           # Вывод оставшегося баланса банковского счета

asyncio.run(main())

# Вывод:
#
# Снятие 900 успешно
# Снятие 900 успешно
# Остаток средств -800