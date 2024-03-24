import asyncio

def not_corutine():
    print('not corutine')

def main():
    task = asyncio.create_task(not_corutine())


main()
