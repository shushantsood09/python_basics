class Person:
    def __init__(self, name, occupation):
        print("Hey I am a person")
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f'{self.name} is a {self.occupation}')

a = Person("Shushant", "Developer")
b = Person("Naman", "Accountant")
a.info()
b.info()

