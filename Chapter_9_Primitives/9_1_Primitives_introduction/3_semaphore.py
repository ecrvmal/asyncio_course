import asyncio

# Создаем экземпляр Semaphore с максимум двумя разрешениями
import random

semaphore = asyncio.Semaphore(2)

async def my_coroutine(id):
    print(f'Корутина {id} хочет получить семафор')
    async with semaphore:
        # Код внутри этого блока будет выполняться только двумя корутинами в один момент времени
        print(f'Корутина {id} получила семафор')
        await asyncio.sleep(random.randint(1,5))
    print(f'Корутина {id} отпустила семафор')

# Запускаем несколько корутин
async def main():
    await asyncio.gather(my_coroutine(1), my_coroutine(2), my_coroutine(3))

asyncio.run(main())

# Корутина 1 хочет получить семафор
# Корутина 1 получила семафор
# Корутина 2 хочет получить семафор
# Корутина 2 получила семафор
# Корутина 3 хочет получить семафор
# Корутина 2 отпустила семафор
# Корутина 3 получила семафор
# Корутина 1 отпустила семафор
# Корутина 3 отпустила семафор

