#simple future example
import asyncio


async def async_operation():
    print("Начало асинхронной операции.")
    await asyncio.sleep(2)
    print("Асинхронная операция успешно завершилась.")


async def main():
    print("Главная корутина запущена.")
    future = asyncio.ensure_future(async_operation())
    await asyncio.sleep(0.1)
    print("Попытка отмены Future.")
    # Отменяем Future до его завершения
    future.cancel()
    try:
        result = await future
        print("Результат Future:", result)
    except asyncio.CancelledError:
        print("Асинхронная операция была отменена в процессе выполнения.")
        # Вновь поднимаем исключение, чтобы передать его дальше
        # raise
        print("Обработка исключения: Future был отменен.")

    if future.cancelled():
        print("Проверка: Future был отменен.")
    else:
        print("Проверка: Future не был отменен.")

    print("Главная корутина завершена.")


asyncio.run(main())