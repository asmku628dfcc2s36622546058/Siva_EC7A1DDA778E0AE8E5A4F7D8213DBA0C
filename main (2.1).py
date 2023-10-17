class BankAccount:
    def __init__(self, account_number, account_holder_name,  initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance
def deposit(self, amount):
    if amount > 0:
        self.__account_balance += amount
        #self.__account_balance b= self.__account_balance+amount
        print("Deposited rs{}. New balance: Rs{}".format(amount,self.__account_balance))
    else:
        print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            self.__account_balance -=amount
            #self.__account_balance = self.__account_balance - amount
            print("Withdraw Rs{}. New baalance: Rs{}".format(amount,self.__account_balance))
        else:
            print("Invalid withhdrawl amount or insufficient balance.")
    def display_balance(self):
        print("Account balance for {} (Account #{}): Rs{}".format(self.__account_holder_name, self.__account_number, self.__account_balance))
#create an instan of the BankAccount class
account = BankAccount(account_number="12334432", account_holder_name="st", initial_balance=5000.0)
#test deposit and withdraw functionally
#account.display_balance()
#account.deposit (500.0)
#account.wihdraw(200.0)
#account.display_balance()