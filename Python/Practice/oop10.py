class Base1:
    def __init__(self):
        print("inside base 1")
        self.A =10

    def fun(self):
        print("Base 1 Fun ")

class Base2:
    def __init__(self):
        print("inside base 2")
        self.B =20

    def fun(self):
        print("Base 2 Gun ")

class Derived(Base1,Base2):
    def __init__(self):
        self.C=30
        Base1.__init__(self)
        Base2.__init__(self)
        print("Inside Derived")

    def sun(self):
        print("Inside Suncls")

def main():
    print("Insinde main ")
    dobj= Derived()
    #dobj.gun()
    Base1(dobj.fun())
    dobj.fun()
    #print(dobj.A)
    #print(dobj.B)
    #print(dobj.C)

if __name__=="__main__":
    main()