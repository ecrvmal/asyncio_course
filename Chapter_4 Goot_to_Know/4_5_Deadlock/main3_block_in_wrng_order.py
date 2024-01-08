# пример блокировки, вызванной получением блокировок в разном порядке

import asyncio


# корутина, выполняющая задачу с использованием блокировок
async def task(number, lock1, lock2):                                 # Объявление асинхронной функции task, принимающей номер задачи и две блокировки
    print(f'Задача {number} приобретает блокировку {lock1}')          # Выводим сообщение о том, что задача пытается приобрести первую блокировку
    async with lock1:                                                 # Используем async with для асинхронного приобретения блокировки. Это обеспечивает, что блокировка будет автоматически освобождена по окончании блока кода
        await asyncio.sleep(1)                                        # Используем sleep() из модуля asyncio для приостановки выполнения на 1 секунду. Это дает время для другой задачи, чтобы она могла приобрести свою первую блокировку
        print(f'Задача {number} приобретает блокировку {lock2}')      # Выводим сообщение о том, что задача пытается приобрести вторую блокировку
        async with lock2:                                             # Аналогично предыдущему, используем async with для асинхронного приобретения второй блокировки
            # сюда никогда не дойдем..
            pass                                                      # Пустой оператор. Используется в качестве заполнителя, когда код еще не написан


async def main():                                                     # Объявление основной асинхронной функции main
    lock1 = asyncio.Lock()                                            # Создаем первую блокировку, используя класс Lock из модуля asyncio
    lock2 = asyncio.Lock()                                            # Создаем вторую блокировку, аналогично первой
    coro1 = task(1, lock1, lock2)                                     # Создаем первую корутину с задачей, передавая в нее номер и две блокировки
    coro2 = task(2, lock2, lock1)                                     # Создаем вторую корутину с задачей, передавая в нее номер и две блокировки, но в обратном порядке
                                                                      # выполняем и ждем завершения обеих корутин
    await asyncio.gather(coro1, coro2)                                # Используем функцию gather() из модуля asyncio для запуска и ожидания завершения обоих корутин


asyncio.run(main())

# Вывод:
#
# Задача 1 приобретает блокировку 1...
# Задача 2 приобретает блокировку 1...
# Задача 1 приобретает блокировку 2...
# Задача 2 приобретает блокировку 2...
# ...
# ...
# ...
#deadlock / бесконечное ожидание корутины / зависание приложения