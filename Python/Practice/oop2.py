
class demo:
    A=10
    B=20

    def __init__(self):
        self.C=30
        self.D=40


def main ():

    print("Value of A : ",demo.A)
    print("Value of B : ",demo.B)

    obj1 = demo()
    obj2= demo()

    print("Value of C from obj1 : ",obj1.C)
    obj1.C = 31
    print("Value of C from obj2: ",obj2.C)
    print("Value of C from obj1 : ",obj1.C)

if __name__=="__main__":
    main()