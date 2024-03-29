# Sample Output:
#
# Искатель приключений начинает путешествие...
# Храбрый рыцарь начинает путешествие...
# Отважный пират начинает путешествие...
# Искатель приключений находит загадочный лес...
# Храбрый рыцарь находит загадочный лес...
# Отважный пират находит загадочный лес...
# Искатель приключений переправляется через реку...
# Храбрый рыцарь переправляется через реку...
# Отважный пират переправляется через реку...
# Искатель приключений встречает дружелюбного дракона...
# Храбрый рыцарь встречает дружелюбного дракона...
# Отважный пират встречает дружелюбного дракона...
# Искатель приключений находит сокровище...
# Храбрый рыцарь находит сокровище...
# Отважный пират находит сокровище...

import asyncio

places = [
   "начинает путешествие",
   "находит загадочный лес",
   "переправляется через реку",
   "встречает дружелюбного дракона",
   "находит сокровище"]

roles = ["Искатель приключений", "Храбрый рыцарь", "Отважный пират"]


async def counter(name, places):
    for pl in places:
        print(f"{name} {pl}...")
        await asyncio.sleep(1)


async def main():
    task1 =asyncio.create_task(counter(roles[0], places))
    task2 =asyncio.create_task(counter(roles[1], places))
    task3 =asyncio.create_task(counter(roles[2], places))

    #Дождитесь выполнения всех созданных задач в главной корутине с помощью await.
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())



