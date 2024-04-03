class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def resetPass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")
print(acc1.acc_no)
# print(acc1.__acc_pass)
acc1.resetPass()


class Person:
    __name = "Amit"

    @staticmethod
    def __hello():
        print("Hello Persin!")

    def welcome(self):
        self.__hello()

p1 = Person()

print(p1.welcome())