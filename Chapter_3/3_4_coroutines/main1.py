import asyncio
# Такой синтаксис является не верным, т.к. все корутины должны запускаться внутри цикла событий

#НЕ ПРАВИЛЬНО
async def example_coroutine():
    print("Hello from coroutine!")

example_coroutine()


#ПРАВИЛЬНО
async def example_coroutine():
    print("Hello from coroutine!")

asyncio.run(example_coroutine())