class account:
    def __init__(self,initial_amt):
        self.blnce=initial_amt
    def deposit(self,amount):
        self.blnce=self.blnce+amount
        return self.blnce
    def withdrawl(self,amount):
        self.blnce=self.blnce-amount
        return self.blnce
ac= account(50000)
dep= account.deposit(ac,70000)
withl= account.withdrawl(ac,80000)
print("Intial Amount       ",50000)
print("\nAfter deposit total amount   ",dep)
print("\nAfter withdrawl the amount left  ",withl)