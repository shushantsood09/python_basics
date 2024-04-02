class Person:
    name = "Shushant"
    occupation = "Software Engineer"
    gender = "Male"

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
a.name = "Naman"
a.occupation = "Accountant"
b.name = "Aman"
b.occupation = "HR"
# print(a.name, a.occupation)
a.info()
b.info()