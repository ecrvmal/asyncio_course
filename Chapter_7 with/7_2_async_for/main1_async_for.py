import asyncio


async def async_gen():                      # Определяем асинхронный генератор async_gen
    for i in range(5):                      # Итерируемся по диапазону чисел от 0 до 4 (5 не включительно)
        await asyncio.sleep(.5)             # Добавляем асинхронную задержку в 0.5 секунды перед каждой итерацией
        yield i                             # Возвращаем текущее число из диапазона с помощью оператора yield


async def main():                           # Определяем асинхронную функцию main
    print(async_gen().__dir__())
    async for number in async_gen():        # Используем асинхронный цикл for для итерации по числам, возвращаемым асинхронным генератором async_gen
        print(number)                       # Выводим текущее число на экран


asyncio.run(main())                         # Запускаем асинхронную функцию main с помощью функции asyncio.run

