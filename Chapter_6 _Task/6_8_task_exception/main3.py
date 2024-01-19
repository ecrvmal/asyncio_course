import asyncio


async def process_item(item):                                           # Асинхронная функция, обрабатывающая один элемент списка
    print(f'{item=}')
    if item == 13 or item == 'i':
        # try:
        raise ValueError(f"Обработка исключения для элемента: {item}")  # Если элемент равен числу 13 или букве 'i', вызываем исключение ValueError
        # except ValueError as _ex:
        #     print(_ex)
    print(f"Элемент соответстует условию: {item}")
    return item


async def process_list(items):                                               # Асинхронная функция, обрабатывающая список элементов
    tasks = [asyncio.create_task(process_item(item)) for item in items]      # Создаем асинхронные задачи для каждого элемента списка с помощью list comprehension
    for task in tasks:                                                       # Цикл для обработки каждой задачи
        try:
            await task                                                       # Если задача успешно завершена, получаем результат
        except Exception as e:
            # task.set_exception(ValueError(f'Установленное исключение {e}'))  # Если задача вызывает исключение ValueError, устанавливаем исключение для задачи и выводим сообщение
            print(task.exception())
    for task in tasks:
        if task.exception():
            print(task.exception())


async def main():                                                             # Асинхронная функция для запуска обработки списка
    items = [13, 2, 13, 4, 13, 'a', 'b', 'c', 'i', 13, 6, 7, 8, 13, 10, 11, 13, 'i', 'e', 'f', 'i', 'h']# Список элементов для обработки
    try:
        await process_list(items)                                                 # Запускаем обработку списка
    except Exception as e:
        print(e)

asyncio.run(main())