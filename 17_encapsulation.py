class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def check_balance(self):
        print(f'{self.name}: {self.__balance}')

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            return 0

    def withdraw(self, amount):
        if amount < 0:
            print('failed')
            return -1
        elif amount > self.__balance:
            print('failed')
            return -2
        else:
            self.__balance = self.__balance - amount
        return 0

# check_balance()
my = BankAccount('John', 1000)
# my.check_balance()
# my.balance
# my.balance = 10000000
# my.balance
# my.check_balance()

# my.check_balance()
# my.deposit(500)
# my.check_balance()
# my.withdraw(2000)
# my.check_balance()
# my.withdraw(200)
# my.check_balance()

print(my._BankAccount__balance)
