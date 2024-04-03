class Person:
    name = "Anonymous"

    # def changeName(self, name):
    #     self.name = name
    #     # self.__class__name = name

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Raman Singhad")
print(p1)
print(Person.name)