

import asyncio

stone_resources_dict = {
    'Каменная плитка': 10,
    'Каменная ваза': 40,
    'Каменный столб': 50,
}

metal_resources_dict = {
    'Металлическая цепь': 6,
    'Металлическая рамка': 24,
    'Металлическая ручка': 54,
}

cloth_resources_dict = {
    'Тканевая занавеска': 8,
    'Тканевый чехол': 24,
    'Тканевое покрывало': 48,
}

stone_condition = asyncio.Condition()
metal_condition = asyncio.Condition()
cloth_condition = asyncio.Condition()
stone_material = 0
metal_material = 0
cloth_material = 0


async def gather_stone():
    global stone_condition
    global stone_material
    while True:
        if stone_completed:
            return
        await asyncio.sleep(1)
        stone_material += 10

    # Добываем камень, 10ед каждую сек.


async def gather_metal():
    # Добываем металл, 6ед каждую сек.


async def gather_cloth():
    # Добываем ткань, 8ед каждую сек.




async def craft_stone_items():
    # Мастерская по крафту из камня


async def craft_metal_items():
    # Мастерская по крафту из мателла


async def craft_cloth_items():
    # Мастерская по крафту из ткани


async def main():
    # Запускаем производства

asyncio.run(main())

