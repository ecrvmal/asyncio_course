import asyncio

# Общий ресурс, который будет обновляться
shared_resource = 0

# Асинхронная функция для обновления общего ресурса
async def update_resource():
    # Используем глобальную переменную shared_resource
    global shared_resource
    print('Начинаем обновление shared_resource')
    # Сохраняем текущее значение shared_resource во временную переменную
    temp = shared_resource
    await asyncio.sleep(1)  # Имитация операции ввода-вывода
    # Увеличиваем значение shared_resource на 1
    shared_resource = temp + 1
    print('Обновление shared_resource завершено')


async def main():
    # Запускаем две асинхронные задачи для обновления shared_resource
    await asyncio.gather(update_resource(), update_resource())
    print(f'shared_resource: {shared_resource}')

asyncio.run(main())