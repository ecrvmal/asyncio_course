import asyncio


# Объявление корутины consumer
async def consumer(condition, name):
    # Блокировка условия
    async with condition:
        # Печатаем сообщение, что потребитель ждет
        print(f'{name} - ждет')

        # Ожидание сигнала
        await condition.wait()

        # Печатаем сообщение, что потребитель проснулся
        print(f'{name} - проснулся')


# Объявление корутины producer
async def producer(condition):
    # Блокировка условия
    async with condition:
        # Печатаем сообщение, что производитель производит
        print('Производитель производит')

        # Уведомление всех ожидающих корутин
        condition.notify_all()


# Объявление корутины main
async def main():
    # Создание условия
    condition = asyncio.Condition()

    # Создание списка корутин-потребителей
    consumers = [asyncio.create_task(consumer(condition, f'Потребитель {i}')) for i in range(3)]

    # Ожидание выполнения всех корутин (производителя и потребителей)
    await asyncio.gather(producer(condition), *consumers)


# Запуск корутины main
asyncio.run(main())


# Потребитель 0 - ждет
# Потребитель 1 - ждет
# Потребитель 2 - ждет
# Производитель производит
# Потребитель 0 - проснулся
# Потребитель 1 - проснулся
# Потребитель 2 - проснулся
