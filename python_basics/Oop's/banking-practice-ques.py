class Account:
    def __init__(self, bal, accNo):
        self.balance = bal
        self.account_no = accNo

    def debit(self, amount):
        self.balance -= amount
        print("Rs:", amount, "was debited")
        print("Total Balance = ", self.getBalance())

    def credit(self, amount):
        self.balance += amount
        print("Rs:", amount, "was debited")
        print("Total Balance = ", self.getBalance())

    def getBalance(self):
        return self.balance

acc1 = Account(10000, 12354)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)
# print(acc1.account_no)
# print(acc1.balance)