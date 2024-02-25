import asyncio

users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank', 'George', 'Helen', 'Ivan', 'Julia']


async def user_action(name, db_condition):
    print(f'Пользователь {name} ожидает доступа к базе данных')
    # async with db_condition:
    await asyncio.sleep(1)
    await db_condition.acquire()
    print(f'Пользователь {name} подключился к БД')

    await asyncio.sleep(0.5)
    # await db_condition.wait()
    print(f'Пользователь {name} отключается от БД')
    db_condition.release()


# async def user_controller(db_condition):
#     while True:
#         await asyncio.sleep(0.6)
#         if db_condition.locked():
#             db_condition.notify(1)

async def main():
    db_condition = asyncio.Condition()
    users_tasks = [asyncio.create_task(user_action(user, db_condition)) for user in users]
    await asyncio.gather(
        # user_controller(db_condition),
        *users_tasks)


asyncio.run(main())

