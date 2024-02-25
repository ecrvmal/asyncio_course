import asyncio
import random

error = None
count = 0
sek = 0

async def monitor_rocket_launches(interrupt_flag):
    global count
    global error
    global sek

    error_case = [False, True]
    try:
        while True:
            error = random.choices(error_case, cum_weights=(75, 25), k=1)
            print(f"Мониторинг ракетных запусков... (Запуск номер {count} прошёл успешно)")
            count += 1
            sek += 1
            await asyncio.sleep(1)
    finally:
        # Поместите сообщение о завершении мониторинга
        "Завершение мониторинга ракетных запусков"


async def main():
    global error
    global count
    global sek

    interrupt_flag = asyncio.Event()
    # Создайте Task задачу
    monitoring = asyncio.create_task(monitor_rocket_launches(interrupt_flag))
    # Допишите сюда цикл
    while True:
        await asyncio.sleep(5)
        count +=1
        if count == 50:
            break
        if error:
            print(f"Ошибка при запуске произошла на {sek} секунде =(")
            print(f"Отмена мониторинга ракетных запусков...")
            break

    # Запустите созданную корутину в пункте 2 через await

if __name__ == "__main__":
    asyncio.run(main())