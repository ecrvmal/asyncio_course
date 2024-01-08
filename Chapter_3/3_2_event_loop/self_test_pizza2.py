import asyncio
from random import randint

class Pizzeria:
    def __init__(self, name):
        self.name = name

    async def make_pizza(self, i):
        time_need = randint(3, 8)
        print(f'Pizzeria "{self.name}" started pizza order {i}, time = {time_need}')
        await asyncio.sleep(time_need)
        print(f'Pizzeria "{self.name}" done  pizza order {i}')


async def main():
    pizzeria = Pizzeria("bread and cheese")
    tasks = [pizzeria.make_pizza(i) for i in range(1,7)]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())