
class Arithmetic:

    def __init__(self):
        self.value1 = 0 
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter value 1 : "))
        self.value2 = int(input("Enter value 2 : "))

    def Addition(self):
        add = 0
        add = self.value1 + self.value2
        return add

    def Subtraction(self):
        sub = 0
        sub = self.value1 - self.value2
        return sub

    def Multiplication(self):
        mult = 0
        mult = self.value1 * self.value2
        return mult

    def Division(self):
        div = 0
        div = self.value1 / self.value2
        return div

def main ():

    Obj1 = Arithmetic()

    Obj1.Accept()
    ret1 = Obj1.Addition()
    ret2 = Obj1.Subtraction()
    ret3 = Obj1.Multiplication()
    ret4 = Obj1.Division()

    print("Addition is : ",ret1)
    print("Subtraction is : ",ret2)
    print("Multiplication is :",ret3)
    print("Division is : ",ret4)

if __name__=="__main__":
    main()