import asyncio

bank_account = 1000

async def cash_withdraw(amount):
    global bank_account
    print(' cash_withdraw started')
    print(f'{bank_account=}')
    await asyncio.sleep(0.5)
    bank_account -= amount
    print(' cash_withdraw completed')

async def main():
    task1 = asyncio.create_task(cash_withdraw(800))
    task2 = asyncio.create_task(cash_withdraw(800))
    await asyncio.gather(task1, task2)
    print(f'{bank_account=}')

asyncio.run(main())