class bank:
    intinal_balance=0
    withdraw_balance=0
    def deposite(self):
       d= int(input("enter the amount you want to deposite = "))
       self.intinal_balance+=d
       print(f"your acount balance is now after update is {self.intinal_balance }")
    def withdraw(self):
        withdraw_balance=int(input("enter the amount you want to withdraw = "))
        if withdraw_balance>self.intinal_balance:
            print("sorry you have isufficent balance")
        else:
             print(f"your withdraw balance is { withdraw_balance} ")
             self.intinal_balance-=withdraw_balance
    def check_balance(self):
         print(f"your remaning account  balane is {self.intinal_balance}")
         
class Deta(bank):
    pass
d=Deta()
d.deposite()
d.withdraw()
d.check_balance()
   
