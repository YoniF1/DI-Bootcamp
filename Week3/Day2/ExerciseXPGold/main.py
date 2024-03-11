
class BankAccount():
    def __init__(self, balance, username, password, authenticated=False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def deposit(self, amount):
        if self.authenticated == False:
            raise Exception("You are not authenticated")

        if amount >= 0:
            self.balance += amount
        else:
            raise Exception("The amount must be a positive integer")
        
    def withdraw(self, amount):
        if self.authenticated == False:
            raise Exception("You are not authenticated")
        
        if amount >= 0:
            self.balance -= amount
        else:
            raise Exception("The amount must be a positive integer")
        
    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
        
class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance > self.minimum_balance:
            self.balance -= amount
        else:
            raise Exception("The balance must be higher than the minimum balance")
            

class ATM():
    def __init__(self, account_list, try_limit):
        self.account_list = [account_list]
        self.try_limit = try_limit
        self.current_tries = 0

    def isinstance(self):
        for object in self.account_list:
            if type(object) == BankAccount or type(object) == MinimumBalanceAccount:
                return True
            else:
                return False
            
    def try_limit_is_positive(self):
        try:
            assert self.try_limit >= 0
        except:
            self.try_limit = 2
            raise Exception("The try limit is not positive")
          

    def show_main_menu(self):
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            self.log_in(username, password)
            return False

    def log_in(self, username, password):
        for account in self.account_list:
            if account.username == username and account.password == password:
                account.authenticated = True
                self.show_account_menu(account)
            else:
                self.current_tries += 1
                if self.current_tries == self.try_limit:
                    print("You've reached the daily try limit")

    def show_account_menu(self, account):
        user_action = input("What would you like to do - deposit, withdraw or exit: ")

        while True:
            if user_action == 'deposit':
                amount = int(input('How much? '))
                account.deposit(amount)
                return False
            elif user_action == 'withdraw':
                amount = int(input('How much? '))
                account.withdraw(amount)
                return False
            elif user_action == 'exit':
                return False
            else:
                True

#Test
                
account = BankAccount(100, 'fred', '123')
atm = ATM(account, 3)
account2 = MinimumBalanceAccount(100, 'steve', '123')
atm2 = ATM(account2, 3)

atm.isinstance()
atm.show_main_menu()
print(account.balance)

atm2.isinstance()
atm2.show_main_menu()
print(account2.balance)
