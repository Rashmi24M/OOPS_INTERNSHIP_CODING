class BankAccount:
    def __init__(self,account_holder):
        self.account_holder=account_holder
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
        print("Deposit completed.New Balance:",self.balance)
    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
            self.display_balance()
           # print("Withdrawal completed.New Balance:",self.balance)

        else:
            print("Insufficient balance")
            
    def display_balance(self):
        print("Current Balance:",self.balance)
            
class SavingsAccount(BankAccount):
    def __init__(self,intrest_rate,account_holder):
        super().__init__(account_holder)
        temp_interest=intrest_rate/100
        self.intrest_rate=temp_interest
    def add_intrest(self):
        #intrest=self.balance*(self.intrest_rate/100)
        self.balance*=(1+self.intrest_rate) #balance *= (1 + interest_rate / 100)

        super().display_balance()
        #print("Intrest added.New Balance:",self.balance)
        
class CurrentAccount(BankAccount):
    def __init__(self,overdraft_limit,account_holder):
        self.overdraft_limit=overdraft_limit
        super().__init__(account_holder)
        
    def withdraw_with_overdraft(self,amount):
        if amount<self.balance+self.overdraft_limit:
            self.balance-=amount
            super().display_balance()
            print("Withdrawal completed.New Balance:",self.balance)
        else:
            print("Exceeds overdraft limit")
            
SA=SavingsAccount(20,"Rashmi")
CA=CurrentAccount(100,"Rashmi")
#SA.deposit(100)
#SA.withdraw(30)
#SA.add_intrest()
#CA.withdraw_with_overdraft(1200)
CA.deposit(500)
CA.withdraw_with_overdraft(590)