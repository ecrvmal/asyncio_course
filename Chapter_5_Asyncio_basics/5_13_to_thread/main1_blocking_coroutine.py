import asyncio
import time


# Блокирующая функция
def blocking_fn():
    print(f"Старт blocking_fn(): {time.strftime('%X')}")
    # Обратите внимание, что time.sleep() может быть заменен любой блокирующей
    # IO-bound операцией, например операцией с файлами.
    time.sleep(1)  # Имитация выполнения длительной операции.
    print(f"Завершение blocking_fn() {time.strftime('%X')}")


# Вызов блокирующей функции
async def fn():
    return blocking_fn()


# Функция асинхронного sleep()
async def sleep_fn():
    print(f"Старт sleep_fn(): {time.strftime('%X')}")
    await asyncio.sleep(1)
    print(f"Завершение sleep_fn() {time.strftime('%X')}")


async def main():
    print(f"Старт main в {time.strftime('%X')}")
    await asyncio.gather(fn(), sleep_fn(), sleep_fn())
    print(f"Завершение main в {time.strftime('%X')}")


start = time.time()
asyncio.run(main())
print(f'Время выполнения программы: {(time.time() - start)}')

