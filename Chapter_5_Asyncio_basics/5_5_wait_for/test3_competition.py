import asyncio

# Словарь бегунов: Имя + скорость бега (м/с)
# Полный список бегунов скрыт под капотом задачи.

runners = {
    "Молния Марк": 12.8,
    "Ветреный Виктор": 13.5,
    "Скоростной Степан": 11.2,
    "Быстрая Белла": 20.0,
}

async def run_lap(name, speed):
    time_needed = float(f'{100/speed:.2f}')
    await asyncio.sleep(time_needed)
    if time_needed % .1 == 0:
        print(f"{name} завершил круг за {time_needed:.1f} секунд")
    else:
        print(f"{name} завершил круг за {time_needed:.2f} секунд")


async def main(max_time=10):  # Максимальное время для завершения круга 10 сек
    tasks = []
    for el in runners.items():
        the_task = asyncio.create_task(run_lap(el[0], el[1]))
        tasks.append(the_task)
    try:
        await asyncio.wait_for(asyncio.gather(*tasks), timeout=max_time)
    except asyncio.TimeoutError:
        pass

max_time = 10
asyncio.run(main())