# Открытие файла в неблокирующем режиме:

import os

def non_blocking_opener(file, flags):
    return os.open(file, flags | os.O_NONBLOCK)

with open('example.txt', 'r', opener=non_blocking_opener) as f:
    content = f.read()