class BankAccount:

    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def display(self):
        print("Account Holder :",self.Name)
        print("Current Balance :",self.Amount)
    
    def deposit(self):
        amount = int(input("Enter deposit amount: "))

        if amount > 0:
            self.Amount += amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self):
        withdrawCarry = int(input("Enter the amount you wanna withdraw: "))
        if withdrawCarry <= 0:
            print("Invalid withdrawal amount")
        else:
            if(self.Amount>=withdrawCarry):
                self.Amount -= withdrawCarry
                print("Withdrawal Successfull")
            else:
                print("Withdrawal Not Possible, Insufficient Balance")
            
    def calculateInterest(self):
        interest = (self.Amount*BankAccount.ROI)/100
        return interest
    
bObj1 = BankAccount("Krishi",5000)
bObj1.display()
bObj1.deposit()
bObj1.display()
bObj1.withdraw()
bObj1.display()
print("Intrest Is: ",bObj1.calculateInterest())


bObj2 = BankAccount("Sahil",10000)
bObj2.display()
bObj2.deposit()
bObj2.display()
bObj2.withdraw()
bObj2.display()
print("Intrest Is: ",bObj2.calculateInterest())


bObj3 = BankAccount("Harsh",0)
bObj3.display()
bObj3.deposit()
bObj3.display()
bObj3.withdraw()
bObj3.display()
print("Intrest Is: ",bObj3.calculateInterest())


bObj4 = BankAccount("Guddu",2000)
bObj4.display()
bObj4.deposit()
bObj4.display()
bObj4.withdraw()
bObj4.display()
print("Intrest Is: ",bObj4.calculateInterest())
    
        