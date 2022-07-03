# Assignemnt 6_3

class Number:

    def __init__(self):
        self.value = int(input("Enter a value : "))

    def CheckPerfect(self):
        if self.value > 0:
            return True
        else:
            return False

    def Factors(self):
        factor =[]
        for i in range(1,self.value+1):
            if self.value % i ==0:
                factor.append(int(i))
        return factor

class Arithmetic(Number):
    def __init__(self):
        Number.__init__(self)

    def CheckPrime(self):
        count = 0
        if self.value > 1:
            for i in range(2,self.value):
                if self.value % i == 0:
                    count = count + 1
            if count > 1:
                return False
            else:
                return True
        else:
            return False        

    def SumFactor(self):
        data = sum(self.Factors())
        return data

def main():
    ret1 = False
    ret3 = False
    Aobj1 = Arithmetic()

    ret1 = Aobj1.CheckPerfect()
    ret2 = Aobj1.Factors()
    ret3 = Aobj1.CheckPrime()
    ret4 = Aobj1.SumFactor()

    print("Check Perfect : ",ret1)
    print("Factor list : ",ret2)
    print("Prime Check : ",ret3)
    print("Sum of Factors : ",ret4)

if __name__=="__main__":
    main()