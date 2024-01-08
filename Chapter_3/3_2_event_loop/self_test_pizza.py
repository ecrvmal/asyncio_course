import asyncio
from random import randint

class Pizzeria:
    def __init__(self, name):
        self.name = name

    async def cooking_pizza(self, order_id):
        cook_time = randint(2,7)
        print(f'Pizzeria "{self.name}" satrted to cook order {order_id}, cooktime: {cook_time}')
        await asyncio.sleep(cook_time)
        print(f'Pizzeria "{self.name}" completed order {order_id}')


async def main():
    pizzeria = Pizzeria('Bread & Cheese')
    tasks = [pizzeria.cooking_pizza(i) for i in range(1,6) ]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())