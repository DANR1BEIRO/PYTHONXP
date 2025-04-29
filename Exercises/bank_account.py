class BankAccount:
    
    """
    Represents a bank account with a holder's name and a balance
    
    Attributes:
    Holder (str): The name of the account holder
    Balance (float): The current balance of the account
    
    Methods:
    Deposit(amount): Deposits a specified amount into the account
    Withdraw(amount): Withdraws a specified amount from the account
    """
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f'Deposit of ${amount:.2f} successfully completed in {self.holder}\'s account!'
        return 'Deposit must be greater than zero'

    def withdraw(self, amount):
        if amount > self.balance:
            return f'Insufficient funds! Current balance: ${self.balance:.2f} in {self.holder}\'s account'
        elif amount > 0:
            self.balance -= amount
            return f'Withdraw of ${amount:.2f} successfully completed in {self.holder}\'s account!'
        return 'Withdraw must be greater than zero'
    
    def __str__(self):
        return f'{self.holder}\'s account - Current balance: ${self.balance:.2f}'
    
def display_accounts(*accounts):
    for account in accounts:
        print(account)

account_1 = BankAccount('Goku', 5000)
account_2 = BankAccount('Gohan', 1500)

print(account_1.withdraw(7000))
print(account_2.deposit(800))
print()
display_accounts(account_1, account_2)
            