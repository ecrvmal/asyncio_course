import asyncio


async def cook_dinner():
    print("Начинаем готовить ужин...")
    await asyncio.sleep(5)  # Представим, что готовка ужина занимает 5 секунд
    print("Ужин готов!")


async def do_laundry():
    print("Начинаем стирку...")
    await asyncio.sleep(7)  # Представим, что стирка занимает 7 секунд
    print("Стирка завершена!")


async def work_on_computer():
    print("Начинаем работу на компьютере...")
    await asyncio.sleep(3)  # Представим, что работа на компьютере занимает 3 секунды
    print("Работа на компьютере завершена!")


# Создаем задачи из сопрограмм

async def main():
    dinner_task = asyncio.create_task(cook_dinner())
    laundry_task = asyncio.create_task(do_laundry())
    computer_task = asyncio.create_task(work_on_computer())

    # Запускаем все задачи одновременно
    # await dinner_task
    # await laundry_task
    # await computer_task


asyncio.run(main())