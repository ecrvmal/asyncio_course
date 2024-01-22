import asyncio

# Корутина имитирует выполнение критической операции
async def my_coroutine():
    print("Агент приступил к выполнению своего задания")
    await asyncio.sleep(1)
    # Если корутина не была отменена выведем это сообщение
    print("Злодей побежден! Миссия успешно завершена!")

# Корутина попытается прервать выполнение защищенной корутины
async def cancel_coroutine(task):
    await asyncio.sleep(0.5)
    task.cancel()
    print("Банг!!! Злодей стреляет в агента!")


async def main():
    # Создаем защищенный shield объект
    shielded_coroutine = asyncio.shield(my_coroutine())
    print("Бронежилет надет на агента")
    cancel_task = asyncio.create_task(cancel_coroutine(shielded_coroutine))
    print("Пистолет злодея заряжен")
    # В случае получения asyncio.CancelledError для shield выводим сообщение
    try:
        await asyncio.gather(shielded_coroutine, cancel_task)
    except asyncio.CancelledError as e:
        print(f'Внимание! Бронежилет разрушен! {e}')
    await asyncio.sleep(1)


asyncio.run(main())