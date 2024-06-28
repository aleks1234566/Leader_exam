class account:
    #  step 1:
     def __init__(self):
          self.name = self
          self.balance = 0
          print("Hello welcome to money depositing machine: ")
    #  step 2
     def deposit(self):
         amount = float(input("Enter amount to be deposited: "))
         self.balance += amount
         print("/n Amount Deposited: ", amount)


     def Withdraw(self):
          amount = float(input("Enter amount to  be witdrawn: "))
          if self.balance >= amount:
               self.balance -= amount
               print("/n You Withdrew: ", amount)
          else:
               print("/n insufficient balance")
        #   step 3
     def display(self):
          print("/n Net avalaible balance = ", self.balance)
        
a = account( )
a.deposit( )
a.Withdraw( )
a.display( )
# step 4
def quit():
    option = input("Do you want to delete your account?, write Y/N: ")
    if option == "Y": 
         print("your account is deleted")
    else:
         print("please make a new transaction")

quit()
 

       