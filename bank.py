

class bank:
    def __init__(self):
        print("Created Bank Account!")
    def show_balance(self):
        global balance = 0
        print(balance)
    def make_account(self):
        accountname = input("Please enter the name you would like for your account.")
    def withdraw(self):
        withdrawal_amount = int(input("How much would you like to withdraw?"))
        if withdrawal_amount > balance:
            print("You don't have enough money in your balance!")
        elif withdrawal_amount <= balance:
            balance = balance - withdrawal_amount
            print("Succesfully withdrew {} dollars!".format(withdrawal_amount))
        else:
            print("Please enter a valid number!")
    def deposit(self):
        deposit_amount = int(input("How much would you like to deposit?"))
        balance = balance + deposit_amount
        print("Succesfully deposited {} dollars!".format(deposit_amount))

dan = bank() 

dan.make_account()
dan.deposit()
dan.withdraw()
dan.show_balance()