
class demo:
    A=10


    def __init__(self):
        self.B=30

    def fun(self):
        print("Inside instance method fun")

    @classmethod
    def gun(cls):
        print("inside Class method")

def main ():
    print("value of class variabe : ",demo.A)

    demo.gun()

    obj1=demo()

    print("vaue of instance vaiable ",obj1.B)
    obj1.fun()
if __name__=="__main__":
    main()