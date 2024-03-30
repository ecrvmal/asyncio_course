# Полный десериализованый JSON вшит в задачу

# вывести информацию о всех отсутствующих книгах,
# 5: Dr. Timothy Gill: Especially his who science. (1993)
# 7: Ashley Gray: Full remain since statement executive. (1992)
# ...

books_json = [
    {
        "Порядковый номер": 1,
        "Автор": "Rebecca Butler",
        "Название": "Three point south wear score organization.",
        "Год издания": "1985",
        "Наличие на полке": True
    },
    {
        "Порядковый номер": 2,
        "Автор": "Mark Cole",
        "Название": "Drive experience customer somebody pressure.",
        "Год издания": "1985",
        "Наличие на полке": False
    },
    ]


import asyncio

async def check_book(book):
    if not book["Наличие на полке"]:
        print(f'{book["Порядковый номер"]}: {book["Автор"]}: {book["Название"]}. ({book["Год издания"]})')

async def main():
    await asyncio.gather(*(check_book(book) for book in books_json))


asyncio.run(main())