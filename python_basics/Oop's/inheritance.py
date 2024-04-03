# # Single level Inheritance
# class Car:
#     color = "Black"
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car Stopped")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("Fortuner")
# car1 = ToyotaCar("Pirus")

# print(car1.start())
# print(car1.color)

# Multi-level Inheritance
class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car Stopped")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.name = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

        

car1 = Fortuner("Diesel")
car1.start()

print(car1.start())
print(car1.color)

# Multiple Inheritance

class A:
    a = "Welcome to class A"

class B:
    b = "Welcome to class B"

class C(A, B):
    c = "Welcome to class C"

c1 = C()

print(c1.a)
print(c1.b)
print(c1.c)
