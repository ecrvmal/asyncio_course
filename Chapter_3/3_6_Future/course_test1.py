#simple future example
import asyncio

async def set_future_result(value, delay):
    print(f"Задача начата. Установка результата '{value}' через {delay} секунд.")
    await asyncio.sleep(delay)
    print("Результат установлен.")
    return value

async def create_and_use_future():
    create_and_use_future(set_future_result("Успех" , 2))

async def main():



asyncio.run(main())