# Вашей задачей является создание двух конкурентно работающих счётчиков, каждый из которых будет останавливаться после достижения определённого числа. Это упражнение поможет вам улучшить понимание использования асинхронных задач и состояний в асинхронном программировании на Python.
#
# Словарь max_counts хранит максимальное значение, до которого каждый счетчик должен быть инкрементирован.
#
# # Counter_1 - имя счётчика
# # 13 - максимальное значение для счётчика Counter_1
#
# max_counts = {
#     "Counter 1": 13,
#     "Counter 2": 7
# }
# Рекомендации:
#
# Создайте словарь counters, где ключи - это имена счётчиков ("Counter 1" и "Counter 2"), а значения - это текущее значение счётчика. Изначально все значения должны быть равны нулю.
# Используйте словарь max_counts, где ключи представляют собой имена счётчиков, а значения - это максимальное число, до которого каждый счётчик должен подсчитать.
# Напишите асинхронную функцию counter, которая принимает имя счётчика и задержку. В цикле эта функция должна увеличивать значение соответствующего счётчика в словаре counters на 1, затем делать паузу на заданное количество секунд, а затем выводить текущее значение счётчика. Этот цикл должен продолжаться до тех пор, пока значение счётчика не достигнет соответствующего значения в словаре max_counts.
# В асинхронной функции main создайте две задачи с использованием asyncio.create_task(), каждая из которых будет выполнять функцию counter с разными именами счётчиков, но с одинаковой задержкой. Это функция должна ожидать завершения обеих задач.
# Вывод вашей программы должен соответствовать полю Sample Output:
#
# Sample Input:
#
# Sample Output:
#
# Counter 1: 1
# Counter 2: 1
# Counter 1: 2
# Counter 2: 2
# Counter 1: 3
# Counter 2: 3
# Counter 1: 4
# Counter 2: 4
# Counter 1: 5
# Counter 2: 5
# Counter 1: 6
# Counter 2: 6
# Counter 1: 7
# Counter 2: 7
# Counter 1: 8
# Counter 1: 9
# Counter 1: 10
# Counter 1: 11
# Counter 1: 12
# Counter 1: 13

import asyncio


async def counter(counter_name, delay=1, max_k=0):
    for k in range(1,max_k+1):
        print(f'{counter_name}: {k}')
        await asyncio.sleep(delay)


async def main():
    max_counts = {
        "Counter 1": 10,
        "Counter 2": 5,
        "Counter 3": 15
    }
    delays = {
        "Counter 1": 1,
        "Counter 2": 2,
        "Counter 3": 0.5
    }

    tasks = []
    for k, v in max_counts.items():
        task = asyncio.create_task(counter(k, delays[k], v))
        tasks.append(task)
    await asyncio.gather(*tasks)


asyncio.run(main())