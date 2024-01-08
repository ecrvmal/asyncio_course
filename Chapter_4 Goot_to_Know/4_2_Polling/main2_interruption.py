import asyncio

async def print_message():
    while True:
        print("Имитация работы функции")                                # Выводим сообщение о работе функции
        await asyncio.sleep(1)                                          # Останавливаем функцию на 1 секунду

async def interrupt_handler(interrupt_flag):
    while True:
        await asyncio.sleep(0.5)                                        # Останавливаем функцию на 0.5 секунды
        if interrupt_flag.is_set():                                     # Если interrupt_flag установлен
            print("Произошло прерывание!, "
                  "в этом месте может быть установлен любой обработчик")# Выводим сообщение о прерывании
            interrupt_flag.clear()                                      # Очищаем interrupt_flag
            break                                                       # Выходим из цикла

async def main():
    interrupt_flag = asyncio.Event()                                    # Создаем флаг interrupt_flag с помощью asyncio.Event
    task1 = asyncio.create_task(print_message())                        # Создаем задачу task1 исполняющую функцию print_message
    task2 = asyncio.create_task(interrupt_handler(interrupt_flag))      # Создаем задачу task2 исполняющую функцию interrupt_handler с interrupt_flag в качестве аргумента
    while True:
        await asyncio.sleep(3)                                          # Останавливаем функцию на 3 секунды
        interrupt_flag.set()                                            # Устанавливаем interrupt_flag
        await task2                                                     # Ожидаем завершения task2
        task2 = asyncio.create_task(interrupt_handler(interrupt_flag))  # Создаем новую задачу task2 с interrupt_flag в качестве аргумента

asyncio.run(main())

