
class Base:
    def __init__(self):
        print("Base Cons")
        self.A = 10

    def fun(self):
        print("Inside Base Function")


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Derived Cons")
        self.B =20

    def gun(self):
        print("Inside Derived Class")

def main ():
    dobj=Derived()
    dobj.fun()
    print(dobj.A)
    

if __name__=="__main__":
    main()