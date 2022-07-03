# Assignemnt 6_2
class BankAccount:

    ROI = 10.5

    def __init__(self):
        self.name = input("Enter name : ")
        self.amount = int(input("Enter amount : "))

    def Display(self):
        print("Name is : ",self.name)
        print("Amount is : ",self.amount)

    def Deposit(self):
        depositAmount= int(input("Enter Deposit amount : "))
        newBalance = self.amount + depositAmount
        return newBalance

    def Withdraw(self):
        withdrawAmount= int(input("Enter Withdraw amount : "))
        newBalance = self.amount - withdrawAmount
        return newBalance

    def CalculateInterest(self):
        intrest = 0.0
        intrest = (self.amount*BankAccount.ROI)/100
        return intrest

def main():
    
    Obj1 = BankAccount()
    
    ret1 = Obj1.Deposit()
    ret2 = Obj1.Withdraw()
    ret3 = Obj1.CalculateInterest()
    Obj1.Display()
    print("New balance after Deposit is : ",ret1)
    print("New balance after withdrawal is : ",ret2)
    print("Intrest is ",ret3)

if __name__=="__main__":
    main()