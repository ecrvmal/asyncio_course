
class Person():
    def __init__(self, age):
        self.age = age


class Men(Person):
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name

    # def __str__(self):
    #     return f'self.age: {self.age}   {self.name=}'

if __name__ == '__main__':
    men = Men(23, 'Ivan')
    print(men)









