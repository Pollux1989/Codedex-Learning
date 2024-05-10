print("#####--------36. Bank Accounts--------#####")

class BankAccount:
    def __init__ (self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def witdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance
    
    def display_balance(self):
        print(f"${self.balance}")
        
Check_Account = BankAccount('Jair', 'Robles', 1234, 'Savings', 9874, 2000)

Check_Account.deposit(200)

Check_Account.display_balance()

Check_Account.witdraw(700)

Check_Account.display_balance()
