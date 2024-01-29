# https://stepik.org/lesson/1022249/step/8?unit=1030276

import asyncio
import itertools
import random

shapes = ["circle", "star", "square", "diamond", "heart"]
colors = ["red", "blue", "green", "yellow", "purple"]
actions = ["change_color", "explode", "disappear"]


async def launch_firework(comb):
    (shape, color, action) = comb
    print(f"Запущен {color} {shape} салют, в форме {action}!!!")
    await asyncio.sleep(random.randint(1,7))
    print(f"Салют {color} {shape} завершил выступление {action}")


async def main():
    combinations = list(itertools.product(shapes, colors, actions))
    tasks = [asyncio.create_task(launch_firework(combi)) for combi in combinations]
    await asyncio.gather(*tasks)


asyncio.run(main())