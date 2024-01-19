
def greetings(txt):
    return f'Hello {txt}'

def farewell(txt):
    return f'bye, {txt}'


def call_back(func, param):
    return func(param)

name = "Student"

result = call_back(greetings, name)
print(result)

result = call_back(farewell, name)
print(result)

