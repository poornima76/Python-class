# Write a bank class, bank account open
# fn, ln , age, balance, balance value is 0 when created
# bank and bank interest rate fixed 12%
# methods: check_balance() which returns the current balance
# deposit_balance()
# withdraw_balance() take the balance and deduct, only in the multiples of 500
# change_interestrate()
# get interest rate, prints the interest rate
# print government holiday list
import sys
class Bank:
    __bank_name = 'Global IME'
    __interest_rate = 0.12

    def __init__(self, first_name, last_name, age):
       self.__first_name = first_name
       self.__last_name = last_name
       self.__age = age
       self.__balance = 0 

    def check_balance(self):
        return self.__balance

    def deposit_balance(self, b):
        if b < 0:
            print('invalid amount entered!')
            return # acts as a break statement so , if the if statement is true, it breaks the statement
        self.__balance = self.__balance + b
        print(f'The deposited amount is {b}')
        print(f'Updated balance is: {self.__balance}')

    def withdraw_balance(self, amount):
        if amount%500 == 0:
            self.__balance = self.__balance - amount
            print(f'The new balance is: {self.__balance}')
        else:
            print('invalid, enter multiples of 500')

    @classmethod
    def change_interest_rate(cls, new_inr_rate):
        Bank.__interest_rate = new_inr_rate
        return Bank.__interest_rate

    @classmethod
    def get_inr_rate(cls):
        return Bank.__interest_rate
    
    @classmethod 
    def get_bank_name(cls):
        return Bank.__bank_name

    @staticmethod
    def govt_holiday():
        print('Dashian')
        print('Tihar')
        print('Udauli Ubhauli')
        print('Loshar')

p = None
while True:
    print(f'Namaste, welcome to {Bank.get_bank_name()}') 
    print('\n')
    print('-'*30) 
    print('******** Menu ***********')
    print('Enter 1 to open account')
    print('Enter 2 to check balance')
    print('Enter 3 to deposit balance')
    print('Enter 4 to withdraw balance')
    print('Enter 5 to get the interest rate')
    print('Enter 6 to change the interest rate')
    print('Enter 7 to print the holiday list')
    print('-'*30) 
    num = int(input('Enter your option: '))
    if num == 1:
        f_name = input('Enter your name: ')
        l_name = input('Enter your last name: ')
        age = input('Enter your age: ')
        p = Bank(f_name, l_name, age)
        print(f'{f_name.title()} {l_name.title()}, your account has been opened.')
    elif num == 2 and p is not None:
       print(p.check_balance())
    elif num == 3 and p is not None:
        p.deposit_balance(40000)
    elif num == 4 and p is not None:
        p.withdraw_balance(3000)
    elif num == 5:
        interest_rate = Bank.get_inr_rate()
        print(f'The interest rate of the bank is: {interest_rate}')
    elif num == 6:
        new_inr = Bank.change_interest_rate(0.15)
        print(f'The new interest rate is: {new_inr}')
    elif num == 7:
        Bank.govt_holiday()
    else:
        print('Invalid entry \n Enter from 1 to 7 only')
        sys.exit()