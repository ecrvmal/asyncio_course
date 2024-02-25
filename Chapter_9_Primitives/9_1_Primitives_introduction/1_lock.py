import asyncio

# Создаем экземпляр Lock
lock = asyncio.Lock()

async def my_coroutine(id):
    print(f'Корутина {id} хочет получить блокировку')
    async with lock:
        # Код внутри этого блока будет выполняться только одной корутиной в один момент времени
        print(f'Корутина {id} получила блокировку')
        await asyncio.sleep(1)
    print(f'Корутина {id} отпустила блокировку')

# Запускаем несколько корутин
async def main():
    await asyncio.gather(my_coroutine(1), my_coroutine(2), my_coroutine(3))

asyncio.run(main())


# Корутина 1 хочет получить блокировку
# Корутина 1 получила блокировку
# Корутина 2 хочет получить блокировку
# Корутина 3 хочет получить блокировку
# Корутина 1 отпустила блокировку
# Корутина 2 получила блокировку
# Корутина 2 отпустила блокировку
# Корутина 3 получила блокировку
# Корутина 3 отпустила блокировку