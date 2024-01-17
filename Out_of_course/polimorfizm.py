class Cat:
    def __init__(self, age):
        self.age = age

    def info(self):
        print('i"m a cat')

    def say(self):
        print('Meaw')


class Dog:
    def __init__(self, age):
        self.age = age

    def info(self):
        print('i"m a dog')

    def say(self):
        print('Gaw')

dog = Dog(2)
cat = Cat(3)
zoo =[dog, cat]
for i in zoo:
    i.info()
    i.say()
