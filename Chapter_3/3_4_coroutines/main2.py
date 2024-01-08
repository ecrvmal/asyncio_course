import asyncio

async def fetch_data():
    await asyncio.sleep(3)
    return "Результат выполнения корутины fetch_data"

async def main():                     # Первая запускаемая корутина, из неё можно запускать остальные и возвращать результат для удобства
    print("Получение данных...")
    data = await fetch_data()
    print("Данные:", data)

asyncio.run(main())     # Точка входа
