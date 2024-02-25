import asyncio

# Создаем экземпляр события
event = asyncio.Event()


# Определяем корутину для ожидания события
async def wait_for_event():
    await asyncio.sleep(1)
    # Выводим сообщение о начале ожидания события
    print('Ждём события')
    # Ожидаем событие
    await event.wait()

    # Выводим сообщение о получении события
    print('Событие получено')


# Определяем корутину для установки события
async def set_event():
    await asyncio.sleep(2)
    # Выводим сообщение о начале установки события
    print('Установка события')

    # Устанавливаем событие
    event.set()


# Определяем главную корутину
async def main():
    # Создаем задачи для корутин wait_for_event и set_event
    task1 = asyncio.create_task(wait_for_event())
    task2 = asyncio.create_task(set_event())

    # Ожидаем завершения обеих задач
    await asyncio.gather(task1, task2)


# Запускаем главную корутину
asyncio.run(main())

# Ждём события
# Установка события
# Событие получено

