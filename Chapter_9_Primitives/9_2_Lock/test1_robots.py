import asyncio
robot_names = ['Электра', 'Механикс', 'Оптимус', 'Симулакр', 'Футуриус']
place_count: int = 0


async def run_robot(lock, num):
    global place_count
    # print(f'Robot {robot_names[num]} awaiting  ')
    async with lock:
        print(f'Робот {robot_names[num]}({num}) передвигается к месту A')
        place_count +=1
        print(f'Робот {robot_names[num]}({num}) достиг места A. Место A посещено {place_count} раз')

async def main():
    lock = asyncio.Lock()
    robots = [asyncio.create_task(run_robot(lock, i)) for i in range(5)]
    await asyncio.gather(*robots)


asyncio.run(main())



