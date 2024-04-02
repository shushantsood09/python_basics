# Example of Abstraction implementation.
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started")

# Here in the above code we hided the background information and just shown the required information.
car1 = Car()
car1.start()