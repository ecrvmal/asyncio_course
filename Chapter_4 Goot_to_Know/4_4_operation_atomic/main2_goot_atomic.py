# Для обеспечения безопасности/атомарности при обновлении общего ресурса используем асинхронный замок asyncio.Lock().
#
#  Замок lock используется для обеспечения того, что только одна корутина может обновлять shared_resource в любой момент времени, предотвращая таким образом условия гонки.

import asyncio

# Общий ресурс, который будет обновляться
shared_resource = 0
# Создаем асинхронный замок для обеспечения безопасности при обновлении shared_resource
lock = asyncio.Lock()


async def update_resource():
    # Используем глобальную переменную shared_resource
    global shared_resource
    print('Начинаем обновление shared_resource')
    # Используем асинхронный замок для обеспечения безопасности при обновлении shared_resource
    async with lock:
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