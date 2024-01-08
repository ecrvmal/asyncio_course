import asyncio

async def do_some_work(x):                           # Объявляем асинхронную функцию do_some_work, принимающую аргумент x
    print(f"Выполнение некоторой работы: {x}")       # Выводим на экран сообщение о начале работы функции с указанием значения x
    await asyncio.sleep(x)                           # Приостанавливаем выполнение на x секунд. Используем asyncio.sleep(x), так как это неблокирующий сон в асинхронном коде
    return x * 2                                     # Возвращаем результат умножения x на 2

async def main():                                    # Объявляем асинхронную функцию main
    future = asyncio.ensure_future(do_some_work(2))  # Создаем Future объект. Этот метод используется для запуска асинхронной функции и не дожидаясь ее завершения, переходим к следующей строке
    result = await future                            # Дожидаемся завершения работы функции и записываем результат в переменную
    print(f"Результат: {result}")                    # Выводим на экран сообщение о результате работы функции

asyncio.run(main())