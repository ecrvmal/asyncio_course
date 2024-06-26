# Словарь с блюдами и временем приготовления в минутах
# Полный список блюд вшит в задачу

dishes = {
    'Куриный суп': 118,
    'Бефстроганов': 13,
    'Рататуй': 49,
    'Лазанья': 108,
    'Паэлья': 51,
    'Утка по-пекински': 41,
}

import asyncio


async def cook_dish(name, duration):
    print(f"Приготовление {name} начато.")
    await asyncio.sleep(duration/10)
    print(f"Приготовление {name} завершено. за {duration / 10}")


async def main():
    tasks = [asyncio.create_task(cook_dish(key, value), name= key) for key, value in dishes.items()]
    done, pending = await asyncio.wait(tasks, timeout=10, return_when=asyncio.ALL_COMPLETED)
    for task in pending:
        print(f"{task.get_name()} не успел(а,о) приготовиться и будет отменено.")
    print(f"\nПриготовлено блюд: {len(done)}. Не успели приготовиться: {len(pending)}.")


asyncio.run(main())

# Приготовление Куриный суп начато.
# Приготовление Бефстроганов начато.
# Приготовление Рататуй начато.
# Приготовление Лазанья начато.
# Приготовление Паэлья начато.
# Приготовление Утка по-пекински начато.
# Приготовление Бефстроганов завершено. за 1.3
# Приготовление Утка по-пекински завершено. за 4.1
# Приготовление Рататуй завершено. за 4.9
# Приготовление Паэлья завершено. за 5.1
# Куриный суп не успел(а,о) приготовиться и будет отменено.
# Лазанья не успел(а,о) приготовиться и будет отменено.
#
# Приготовлено блюд: 4. Не успели приготовиться: 2.
