import aiocsv
import csv
import asyncio
import aiofiles


class CustomDialect(csv.Dialect):
    delimiter = ';'                         # Определяет символ-разделитель столбцов в csv файле как ";"
    quotechar = '"'                         # Определяет символ кавычек, используемый для обрамления полей в csv файле, как двойные кавычки ("")
    doublequote = True                      # Если этот параметр True, две кавычки внутри поля трактуются как одна кавычка
    skipinitialspace = True                 # Если параметр True, пробелы в начале каждого поля игнорируются
    lineterminator = '\n'                   # Определяет символ окончания строки в csv файле как "\n"
    quoting = csv.QUOTE_MINIMAL             # Указывает, что кавычки должны окружать только те поля, которые содержат специальные символы (например, разделитель, кавычки или любой из символов новой строки)


csv.register_dialect('customDialect', CustomDialect) # Регистрирует диалект с именем 'customDialect' для последующего использования в csv.reader или csv.writer

async def read_csv_file():
    async with aiofiles.open('file.csv', mode='r') as f:
        reader = aiocsv.AsyncReader(f, dialect='customDialect')
        async for row in reader:
            print(row)

asyncio.run(read_csv_file())
